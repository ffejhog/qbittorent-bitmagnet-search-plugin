# Quick Start Guide

Get started with the Bitmagnet qBittorrent search plugin in 5 minutes!

## Prerequisites

- ✅ Bitmagnet installed and running (default: http://localhost:3333)
- ✅ qBittorrent 4.1.0 or later installed
- ✅ Python 3.7+ installed on your system

## Installation Steps

### 1. Download the Plugin

Download `bitmagnet.py` from the repository or releases page.

### 2. Install in qBittorrent

**Option A: Via qBittorrent UI (Easiest)**

1. Open qBittorrent
2. Press `F3` or go to **View** → **Search Engine**
3. Click **Search plugins...** (bottom right)
4. Click **Install a new one** → **Local file**
5. Browse to and select `bitmagnet.py`
6. Click **OK**

**Option B: Manual Installation**

Copy `bitmagnet.py` to:
- **Windows**: `%LOCALAPPDATA%\qBittorrent\nova3\engines\`
- **Linux**: `~/.local/share/qBittorrent/nova3/engines/`
- **macOS**: `~/Library/Application Support/qBittorrent/nova3/engines/`

### 3. Verify Installation

1. Open qBittorrent Search (F3)
2. Look for "Bitmagnet" in the search engines list
3. Check the checkbox next to "Bitmagnet"

### 4. First Search

1. Enter a search term (e.g., "ubuntu")
2. Make sure "Bitmagnet" is checked
3. Click **Search**

## Configuration

### Default Setup (Localhost)

If Bitmagnet is running on `http://localhost:3333`, no configuration needed! The plugin works out of the box.

### Custom Configuration

Edit `bitmagnet.json` in the plugin directory:

**Linux/macOS:**
```bash
cd ~/.local/share/qBittorrent/nova3/engines/
nano bitmagnet.json
```

**Windows:**
```
notepad %LOCALAPPDATA%\qBittorrent\nova3\engines\bitmagnet.json
```

**Example Configuration:**
```json
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

### Remote Bitmagnet Server

```json
{
    "api_url": "http://192.168.1.100:3333/graphql",
    "base_url": "http://192.168.1.100:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

## Testing

### Test from Command Line

```bash
# Linux/macOS
cd ~/.local/share/qBittorrent/nova3/engines/
python3 nova2.py bitmagnet all "ubuntu"

# Windows
cd %LOCALAPPDATA%\qBittorrent\nova3\engines\
python nova2.py bitmagnet all "ubuntu"
```

Expected output:
```
magnet:?xt=urn:btih:ABC123...|ubuntu-22.04-desktop-amd64.iso|3.61 GB|150|25|http://localhost:3333|http://localhost:3333/#/torrents/ABC123...
```

### Category Testing

```bash
# Search movies
python3 nova2.py bitmagnet movies "the matrix"

# Search TV shows
python3 nova2.py bitmagnet tv "breaking bad"

# Search music
python3 nova2.py bitmagnet music "pink floyd"

# Search books
python3 nova2.py bitmagnet books "python programming"

# Search games
python3 nova2.py bitmagnet games "portal"

# Search software
python3 nova2.py bitmagnet software "linux"

# Search adult content only (xxx category - command line only)
python3 nova2.py bitmagnet xxx "search term"

# Search everything including unclassified (unknown category - command line only)
python3 nova2.py bitmagnet unknown "search term"
```

**Note:** The `xxx` and `unknown` categories are available via command line but won't appear in qBittorrent's UI dropdown (non-standard categories).

**Tip:** The "All" category in qBittorrent UI now searches everything (including xxx and unclassified content).

## Troubleshooting

### ❌ "Cannot connect to Bitmagnet"

**Check Bitmagnet is running:**
```bash
curl http://localhost:3333/graphql
```

**Expected response:** GraphQL introspection or error about missing query

**If it fails:**
- Start Bitmagnet: `docker-compose up -d` or `bitmagnet worker run --all`
- Check port 3333 is not blocked
- Verify `api_url` in `bitmagnet.json`

### ❌ No Results

**Possible causes:**
1. Bitmagnet hasn't indexed any torrents yet
2. Search term too specific
3. Category filter excluding results

**Solutions:**
- Check Bitmagnet web UI: http://localhost:3333
- Wait for DHT crawler to index torrents
- Try broader search terms
- Search "All" category first

### ❌ Plugin Not Appearing in qBittorrent

**Solutions:**
1. Restart qBittorrent completely
2. Check plugin is in correct directory
3. Verify Python is installed and in PATH
4. Check file is named exactly `bitmagnet.py`

### ❌ "Malformed configuration file"

**Solution:** Delete `bitmagnet.json` and restart qBittorrent. The plugin will create a fresh config.

## Usage Tips

### 🎯 Better Search Results

1. **Use specific terms**: "Ubuntu 22.04" instead of "linux"
2. **Use quotes**: "breaking bad s01e01" for exact matches
3. **Try categories**: Filter by Movies/TV/Music for focused results
4. **Be patient**: First search may be slow while Bitmagnet builds index

### 📊 Understanding Results

- **Seeds**: Number of peers with complete file (higher = faster download)
- **Leech**: Number of peers downloading (indicates popularity)
- **Size**: File size (check if it matches expectations)
- **Name**: Torrent name (look for release group, quality indicators)

### ⚡ Performance

**For faster searches (fewer results):**
```json
{
    "results_per_page": 50,
    "max_pages": 5
}
```

**For comprehensive searches:**
```json
{
    "results_per_page": 100,
    "max_pages": 20
}
```

## Next Steps

1. ⭐ Star the repository if you find it useful
2. 📖 Read the full [README.md](README.md) for advanced features
3. 🐛 Report issues on GitHub
4. 💡 Request features or contribute improvements

## Support

- **Plugin Issues**: [GitHub Issues](https://github.com/bitmagnet-io/bitmagnet-qbittorrent-search-plugin/issues)
- **Bitmagnet Help**: [Bitmagnet Docs](https://bitmagnet.io)
- **qBittorrent Help**: [qBittorrent Forums](https://qbforums.shiki.hu/)

## Version

This guide is for Bitmagnet qBittorrent Search Plugin v1.0

---

**Happy Searching! 🔍**
