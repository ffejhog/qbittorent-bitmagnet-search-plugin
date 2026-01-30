# Bitmagnet Search Plugin for qBittorrent

A qBittorrent search plugin that integrates with [Bitmagnet](https://bitmagnet.io), a self-hosted BitTorrent indexer, DHT crawler, and torrent search engine.

## Features

- 🔍 Search your local Bitmagnet instance directly from qBittorrent
- 🎯 Category filtering (Movies, TV Shows, Music, Books, Games, Software, Anime)
- 📊 Displays seeders, leechers, and torrent size
- 🔗 Direct magnet links for instant downloads
- ⚙️ Configurable via JSON file
- 📄 Pagination support for large result sets

## Requirements

- qBittorrent 4.1.0 or later
- Python 3.7 or later
- Running Bitmagnet instance (local or remote)

## Installation

### Method 1: Through qBittorrent UI (Recommended)

1. Download `bitmagnet.py` from this repository
2. Open qBittorrent
3. Go to **View** → **Search Engine** (or press F3)
4. Click **Search plugins...** button at bottom right
5. Click **Install a new one** → **Local file**
6. Select the downloaded `bitmagnet.py` file
7. Click **OK**

### Method 2: Manual Installation

1. Download `bitmagnet.py` from this repository
2. Copy it to your qBittorrent search engines directory:
   - **Windows**: `%LOCALAPPDATA%\qBittorrent\nova3\engines\`
   - **Linux**: `~/.local/share/qBittorrent/nova3/engines/`
   - **macOS**: `~/Library/Application Support/qBittorrent/nova3/engines/`
3. Restart qBittorrent

## Configuration

On first run, the plugin creates a `bitmagnet.json` configuration file in the same directory as the plugin.

### Default Configuration

```json
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `api_url` | Bitmagnet GraphQL API endpoint | `http://localhost:3333/graphql` |
| `base_url` | Bitmagnet web UI base URL | `http://localhost:3333` |
| `results_per_page` | Number of results per page | `100` |
| `max_pages` | Maximum pages to fetch | `10` |

### Remote Bitmagnet Instance

To use a remote Bitmagnet instance, edit `bitmagnet.json`:

```json
{
    "api_url": "http://192.168.1.100:3333/graphql",
    "base_url": "http://192.168.1.100:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

## Supported Categories

The plugin maps qBittorrent categories to Bitmagnet content types:

| qBittorrent Category | Bitmagnet Content Types | Notes |
|---------------------|------------------------|-------|
| All | **Everything** (no filter) | Includes all content types + unclassified torrents |
| Movies | Movies | |
| TV | TV Shows | |
| Anime | TV Shows | |
| Music | Music | |
| Books | E-books, Comics, Audiobooks | |
| Games | Games | |
| Software | Software | |
| Pictures | *(Not supported - no results)* | No mapping |
| **XXX** | **Adult Content** | **⚠️ Non-standard category** |
| **Unknown** | **Everything** (no filter) | **⚠️ Non-standard category** |

### About Non-Standard Categories

#### XXX Category
The `xxx` category allows searching specifically for adult content:

- ✅ **Available via command line**: `python nova2.py bitmagnet xxx "search term"`
- ⚠️ **Not visible in qBittorrent UI**: Won't appear in the category dropdown
- 🔍 **Filtered**: Returns only adult content

#### Unknown Category
The `unknown` category searches all content without any content type filter:

- ✅ **Available via command line**: `python nova2.py bitmagnet unknown "search term"`
- ⚠️ **Not visible in qBittorrent UI**: Won't appear in the category dropdown
- 🔍 **Unfiltered**: Same as "All" - includes everything (classified + unclassified + xxx)
- 💡 **Use case**: When you want to ensure you're searching absolutely everything

**Note:** The "All" category now includes ALL content types including xxx and unclassified torrents.

## Usage

### In qBittorrent

1. Open the Search tab (F3)
2. Enable "Bitmagnet" in the search plugins dropdown
3. Enter your search query
4. Select a category (optional)
5. Click Search

### Command Line Testing

You can test the plugin from command line using qBittorrent's search engine framework:

```bash
# Navigate to plugin directory
cd ~/.local/share/qBittorrent/nova3/engines/  # Linux
# or
cd %LOCALAPPDATA%\qBittorrent\nova3\engines\  # Windows

# Run test searches
python nova2.py bitmagnet all "ubuntu"
python nova2.py bitmagnet movies "the matrix"
python nova2.py bitmagnet tv "breaking bad"
python nova2.py bitmagnet books "python programming"

# Adult content (xxx category - command line only)
python nova2.py bitmagnet xxx "search term"
```

## Output Format

Results are displayed in qBittorrent's standard format:

- **Name**: Torrent name
- **Size**: File size (KB/MB/GB/TB)
- **Seeds**: Number of seeders
- **Leech**: Number of leechers
- **Engine**: Bitmagnet (with link to your instance)

Each result includes:
- Direct magnet link for downloading
- Link to torrent details in Bitmagnet web UI

## Troubleshooting

### "Cannot connect to Bitmagnet" Error

**Problem**: Plugin cannot reach Bitmagnet server

**Solutions**:
1. Verify Bitmagnet is running: `curl http://localhost:3333/graphql`
2. Check `bitmagnet.json` has correct URLs
3. Ensure firewall allows connection
4. For remote instances, verify network connectivity

### No Results Returned

**Problem**: Search completes but shows no results

**Solutions**:
1. Try the same search in Bitmagnet web UI
2. Check if your Bitmagnet instance has indexed content
3. Try broader search terms
4. Check category filters aren't too restrictive

### "Malformed configuration file" Error

**Problem**: Configuration file has invalid JSON

**Solutions**:
1. Delete `bitmagnet.json` - plugin will recreate it
2. Validate JSON syntax at https://jsonlint.com
3. Ensure proper quotes and commas in JSON

### Pictures Category Returns Nothing

**Expected behavior**: Bitmagnet doesn't have a "pictures" content type, so this category returns no results. Use the web UI to filter by image file types instead.

## Advanced Usage

### Limiting Results

To reduce API load or search time, adjust `max_pages`:

```json
{
    "max_pages": 5,
    "results_per_page": 50
}
```

This limits searches to 250 results maximum (5 pages × 50 results).

### Performance Tuning

For faster searches with smaller result sets:

```json
{
    "results_per_page": 50,
    "max_pages": 4
}
```

For comprehensive searches:

```json
{
    "results_per_page": 100,
    "max_pages": 20
}
```

## Development

### File Structure

```
bitmagnet-qbittorrent-search-plugin/
├── bitmagnet.py         # Main plugin file
├── bitmagnet.json       # Configuration (created on first run)
├── README.md            # This file
├── LICENSE              # MIT License
└── examples/            # Usage examples
```

### Testing Without qBittorrent

Download the nova3 test files from qBittorrent repository:

```bash
# Download test framework
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/nova2.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/helpers.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/novaprinter.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/socks.py

# Run test
python nova2.py bitmagnet all "test query"
```

### API Reference

The plugin uses Bitmagnet's GraphQL API:

**Query**: `TorrentContentSearch`
**Endpoint**: `/graphql` (default port 3333)

**Input Variables**:
- `queryString`: Search terms
- `limit`: Results per page
- `offset`: Pagination offset
- `facets.contentType.filter`: Array of content types

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - See LICENSE file for details

## Credits

- **Plugin Author**: Bitmagnet Community
- **Bitmagnet**: https://bitmagnet.io
- **qBittorrent**: https://www.qbittorrent.org

## Support

- **Issues**: https://github.com/bitmagnet-io/bitmagnet-qbittorrent-search-plugin/issues
- **Bitmagnet Docs**: https://bitmagnet.io
- **qBittorrent Search Plugins**: https://github.com/qbittorrent/search-plugins

## Changelog

### Version 1.0 (2024-01-30)
- Initial release
- GraphQL API integration
- Category filtering
- Configurable via JSON
- Pagination support
- Error handling and logging
