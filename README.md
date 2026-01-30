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

### Via qBittorrent UI (Recommended)

1. Download `bitmagnet.py` from this repository
2. Open qBittorrent
3. Go to **View** → **Search Engine** (or press F3)
4. Click **Search plugins...** button at bottom right
5. Click **Install a new one** → **Local file**
6. Select the downloaded `bitmagnet.py` file
7. Click **OK**

### Manual Installation

Copy `bitmagnet.py` to your qBittorrent search engines directory:

- **Windows**: `%LOCALAPPDATA%\qBittorrent\nova3\engines\`
- **Linux**: `~/.local/share/qBittorrent/nova3/engines/`
- **macOS**: `~/Library/Application Support/qBittorrent/nova3/engines/`

Then restart qBittorrent.

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

## Category Mapping

| qBittorrent Category | Bitmagnet Content Types |
|---------------------|------------------------|
| All | No filter (all content) |
| Movies | movie |
| TV | tv_show |
| Anime | tv_show |
| Music | music |
| Books | ebook, comic, audiobook |
| Games | game |
| Software | software |
| Pictures | *(not supported)* |
| XXX | xxx |

## Usage

### In qBittorrent

1. Open the Search tab (F3)
2. Enable "Bitmagnet" in the search plugins dropdown
3. Enter your search query
4. Select a category (optional)
5. Click Search

### Command Line Testing

```bash
cd ~/.local/share/qBittorrent/nova3/engines/  # Linux
python3 nova2.py bitmagnet all "ubuntu"
python3 nova2.py bitmagnet movies "the matrix"
```

## Troubleshooting

### "Cannot connect to Bitmagnet" Error

1. Verify Bitmagnet is running: `curl http://localhost:3333/graphql`
2. Check `bitmagnet.json` has correct URLs
3. Ensure firewall allows connection

### No Results Returned

1. Try the same search in Bitmagnet web UI
2. Check if your Bitmagnet instance has indexed content
3. Try broader search terms

### "Malformed configuration file" Error

Delete `bitmagnet.json` and restart qBittorrent. The plugin will recreate it with defaults.

## Development

### Testing Without qBittorrent

Download the nova3 test files from qBittorrent repository:

```bash
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/nova2.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/helpers.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/novaprinter.py
wget https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/socks.py

python3 nova2.py bitmagnet all "test query"
```

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Credits

- **Bitmagnet**: https://bitmagnet.io
- **qBittorrent**: https://www.qbittorrent.org
- **qBittorrent Search Plugins**: https://github.com/qbittorrent/search-plugins
