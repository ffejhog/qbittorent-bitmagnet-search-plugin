# Configuration Examples

This directory contains example configuration files for different use cases.

## Files

### `bitmagnet.json.example`
Default configuration for local Bitmagnet instance on standard port.
- Use when: Bitmagnet running on same machine as qBittorrent
- Copy to: `bitmagnet.json` in plugin directory

### `bitmagnet-remote.json.example`
Configuration for remote Bitmagnet server.
- Use when: Bitmagnet running on different machine/IP
- Update IP address to match your server
- Copy to: `bitmagnet.json` in plugin directory

### `bitmagnet-fast.json.example`
Optimized for faster searches with fewer results.
- Smaller page size (50 instead of 100)
- Fewer pages (5 instead of 10)
- Maximum 250 results total
- Use when: You want quick results and don't need comprehensive searches

## How to Use

1. Choose the example that matches your setup
2. Copy to plugin directory as `bitmagnet.json`:

**Linux/macOS:**
```bash
cp bitmagnet.json.example ~/.local/share/qBittorrent/nova3/engines/bitmagnet.json
```

**Windows:**
```powershell
copy bitmagnet.json.example %LOCALAPPDATA%\qBittorrent\nova3\engines\bitmagnet.json
```

3. Edit the file to customize settings if needed
4. Restart qBittorrent or reload search plugins

## Configuration Options

| Option | Description | Default | Range |
|--------|-------------|---------|-------|
| `api_url` | GraphQL API endpoint | `http://localhost:3333/graphql` | Any valid URL |
| `base_url` | Web UI base URL | `http://localhost:3333` | Any valid URL |
| `results_per_page` | Results per page | `100` | 1-100 recommended |
| `max_pages` | Maximum pages to fetch | `10` | 1-50 |

## Custom Configurations

### High Performance (Local SSD, Fast Network)
```json
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 20,
    "results_per_page": 100
}
```
- Maximum 2000 results
- Best for comprehensive searches

### Limited Bandwidth
```json
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 3,
    "results_per_page": 30
}
```
- Maximum 90 results
- Reduces API calls and data transfer

### Remote Server (VPN)
```json
{
    "api_url": "https://bitmagnet.myserver.com/graphql",
    "base_url": "https://bitmagnet.myserver.com",
    "max_pages": 10,
    "results_per_page": 100
}
```
- Use HTTPS for security
- Works with reverse proxy setups
- Update domain to match your server

## Troubleshooting

### Invalid JSON Error
- Validate your JSON at https://jsonlint.com
- Check for missing commas or quotes
- Ensure no trailing commas

### Connection Issues
- Verify `api_url` is correct
- Test with: `curl <api_url>`
- Check firewall rules
- Ensure Bitmagnet is running

### Slow Searches
- Reduce `results_per_page` to 50
- Reduce `max_pages` to 5
- Check Bitmagnet server performance
