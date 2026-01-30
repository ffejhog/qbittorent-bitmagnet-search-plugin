# VERSION: 1.0
# AUTHORS: Bitmagnet Community
# LICENSING: MIT

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Any, Dict, List, Optional

from novaprinter import prettyPrinter

CONFIG_FILE = 'bitmagnet.json'
CONFIG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), CONFIG_FILE)
CONFIG_DATA: Dict[str, Any] = {
    'api_url': 'http://localhost:3333/graphql',
    'base_url': 'http://localhost:3333',
    'results_per_page': 100,
    'max_pages': 10,
}


def load_configuration() -> None:
    """Load configuration from JSON file or create default if missing."""
    try:
        with open(CONFIG_PATH, encoding='utf-8') as f:
            user_config = json.load(f)
            CONFIG_DATA.update(user_config)
    except FileNotFoundError:
        save_configuration()
    except json.JSONDecodeError:
        CONFIG_DATA['malformed'] = True
        sys.stderr.write(f"Error: Malformed configuration file at {CONFIG_PATH}\n")
    except Exception as e:  # pylint: disable=broad-exception-caught
        sys.stderr.write(f"Error loading configuration: {e}\n")


def save_configuration() -> None:
    """Save default configuration to JSON file."""
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            config_to_save = {k: v for k, v in CONFIG_DATA.items() if k != 'malformed'}
            f.write(json.dumps(config_to_save, indent=4, sort_keys=True))
    except Exception as e:  # pylint: disable=broad-exception-caught
        sys.stderr.write(f"Error saving configuration: {e}\n")


load_configuration()


class bitmagnet:
    """Bitmagnet search plugin for qBittorrent."""

    name = 'Bitmagnet'
    url = CONFIG_DATA.get('base_url', 'http://localhost:3333')
    supported_categories = {
        'all': '0',
        'movies': '1',
        'tv': '2',
        'anime': '3',
        'music': '4',
        'books': '5',
        'games': '6',
        'software': '7',
        'pictures': '8',
        'xxx': '9',
    }

    CATEGORY_MAP: Dict[str, Optional[List[str]]] = {
        'all': None,
        'movies': ['movie'],
        'tv': ['tv_show'],
        'anime': ['tv_show'],
        'music': ['music'],
        'books': ['ebook', 'comic', 'audiobook'],
        'games': ['game'],
        'software': ['software'],
        'pictures': [],
        'xxx': ['xxx'],
    }

    def __init__(self) -> None:
        self.api_url: str = CONFIG_DATA.get('api_url', 'http://localhost:3333/graphql')
        self.base_url: str = CONFIG_DATA.get('base_url', 'http://localhost:3333')
        self.results_per_page: int = CONFIG_DATA.get('results_per_page', 100)
        self.max_pages: int = CONFIG_DATA.get('max_pages', 10)

        if CONFIG_DATA.get('malformed', False):
            sys.stderr.write("Error: Configuration file is malformed. Using defaults.\n")

    def search(self, what: str, cat: str = 'all') -> None:
        """Perform search and output results via prettyPrinter."""
        what = urllib.parse.unquote(what)
        content_types = self.CATEGORY_MAP.get(cat.lower(), self.CATEGORY_MAP['all'])

        if content_types is not None and len(content_types) == 0:
            return

        offset = 0
        page = 0
        max_results = self.results_per_page * self.max_pages

        while offset < max_results and page < self.max_pages:
            try:
                results = self._graphql_search(what, content_types, offset)

                if not results or 'items' not in results:
                    break

                for item in results['items']:
                    formatted = self._format_result(item)
                    if formatted:
                        prettyPrinter(formatted)

                if not results.get('hasNextPage', False):
                    break

                offset += self.results_per_page
                page += 1

            except Exception as e:  # pylint: disable=broad-exception-caught
                sys.stderr.write(f"Bitmagnet search error: {e}\n")
                break

    def _graphql_search(self, query_string: str, content_types: Optional[List[str]], offset: int) -> Optional[Dict[str, Any]]:
        """Execute GraphQL search query against Bitmagnet API."""
        graphql_query = """
        query TorrentContentSearch($input: TorrentContentSearchQueryInput!) {
          torrentContent {
            search(input: $input) {
              items {
                infoHash
                title
                seeders
                leechers
                publishedAt
                torrent {
                  name
                  size
                  magnetUri
                }
              }
              hasNextPage
              totalCount
            }
          }
        }
        """

        variables: Dict[str, Any] = {
            "input": {
                "queryString": query_string,
                "limit": self.results_per_page,
                "offset": offset,
                "hasNextPage": True,
            }
        }

        if content_types:
            variables["input"]["facets"] = {
                "contentType": {
                    "filter": content_types
                }
            }

        payload = {
            "query": graphql_query,
            "variables": variables
        }

        try:
            data = json.dumps(payload).encode('utf-8')
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }

            request = urllib.request.Request(
                self.api_url,
                data=data,
                headers=headers,
                method='POST'
            )

            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))

                if 'errors' in result:
                    sys.stderr.write(f"GraphQL errors: {result['errors']}\n")
                    return None

                if 'data' in result and 'torrentContent' in result['data']:
                    return result['data']['torrentContent']['search']

                return None

        except urllib.error.URLError as e:
            sys.stderr.write(f"Cannot connect to Bitmagnet at {self.api_url}: {e}\n")
            return None
        except json.JSONDecodeError as e:
            sys.stderr.write(f"Invalid JSON response from Bitmagnet: {e}\n")
            return None
        except Exception as e:  # pylint: disable=broad-exception-caught
            sys.stderr.write(f"Unexpected error querying Bitmagnet: {e}\n")
            return None

    def _format_result(self, item: Dict[str, Any]) -> Optional[Dict[str, str]]:
        """Format a GraphQL result into qBittorrent search result format."""
        try:
            torrent = item.get('torrent', {})

            magnet_uri = torrent.get('magnetUri', '')
            name = torrent.get('name', item.get('title', 'Unknown'))
            size_bytes = torrent.get('size', 0)
            seeders = item.get('seeders')
            leechers = item.get('leechers')
            info_hash = item.get('infoHash', '')
            published_at = item.get('publishedAt', '')

            if not magnet_uri:
                return None

            size_str = self._format_size(size_bytes)
            seeds_str = str(seeders) if seeders is not None else '-1'
            leech_str = str(leechers) if leechers is not None else '-1'
            pub_date_str = self._format_date(published_at)
            desc_link = f"{self.base_url}/#/torrents/{info_hash}" if info_hash else self.base_url

            return {
                'link': magnet_uri,
                'name': name,
                'size': size_str,
                'seeds': seeds_str,
                'leech': leech_str,
                'engine_url': self.base_url,
                'desc_link': desc_link,
                'pub_date': pub_date_str,
            }

        except Exception as e:  # pylint: disable=broad-exception-caught
            sys.stderr.write(f"Error formatting result: {e}\n")
            return None

    def _format_size(self, size_bytes: int) -> str:
        """Convert bytes to human-readable size string."""
        try:
            size = int(size_bytes)
            if size < 0:
                return "-1"
            for unit, threshold in [('B', 1024), ('KB', 1024**2), ('MB', 1024**3), ('GB', 1024**4)]:
                if size < threshold:
                    divisor = threshold // 1024 if unit != 'B' else 1
                    return f"{size / divisor:.2f} {unit}" if unit != 'B' else f"{size} {unit}"
            return f"{size / (1024**4):.2f} TB"
        except (ValueError, TypeError):
            return "-1"

    def _format_date(self, date_str: str) -> str:
        """Convert ISO 8601 date string to Unix timestamp."""
        if not date_str:
            return "-1"

        try:
            if date_str.endswith('Z'):
                date_str = date_str[:-1] + '+00:00'

            try:
                dt = datetime.fromisoformat(date_str)
            except ValueError:
                if '.' in date_str:
                    date_str = date_str.split('.')[0] + date_str.split('.')[-1][-6:]
                dt = datetime.fromisoformat(date_str)

            return str(int(dt.timestamp()))

        except Exception:  # pylint: disable=broad-exception-caught
            return "-1"

    def download_torrent(self, info: str) -> None:
        """Handle torrent download (magnet links only)."""
        if info.startswith('magnet:?'):
            print(f"{info} {info}")
        else:
            print(info)
