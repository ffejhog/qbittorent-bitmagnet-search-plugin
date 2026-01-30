# Installation Guide

Complete installation instructions for the Bitmagnet qBittorrent search plugin.

## System Requirements

### Required
- **qBittorrent**: Version 4.1.0 or later
- **Python**: Version 3.7 or later
- **Bitmagnet**: Running instance (local or remote)

### Supported Platforms
- ✅ Windows 10/11
- ✅ Linux (Ubuntu, Debian, Fedora, Arch, etc.)
- ✅ macOS 10.14 or later
- ✅ FreeBSD

## Pre-Installation Checklist

Before installing, verify:

1. **Bitmagnet is running**
   ```bash
   curl http://localhost:3333/graphql
   ```
   Should return HTML or GraphQL error (not connection refused)

2. **qBittorrent is installed**
   ```bash
   qbittorrent --version
   ```

3. **Python is available**
   ```bash
   python3 --version
   ```
   Should show Python 3.7 or later

## Installation Methods

### Method 1: qBittorrent UI (Recommended for Beginners)

**Step 1:** Download the plugin
- Download `bitmagnet.py` from the repository
- Save it somewhere accessible (e.g., Downloads folder)

**Step 2:** Open qBittorrent Search
- Launch qBittorrent
- Press `F3` or go to **View** → **Search Engine**
- The search tab should appear at the bottom

**Step 3:** Open Plugin Manager
- Click the **Search plugins...** button (bottom-right corner)
- A new window will open showing installed plugins

**Step 4:** Install Plugin
- Click **Install a new one**
- Select **Local file**
- Browse to and select `bitmagnet.py`
- Click **Open** or **OK**

**Step 5:** Verify Installation
- Plugin should appear in the list as "Bitmagnet v1.0"
- Close the plugins window
- In search tab, check the box next to "Bitmagnet"

**Done!** The plugin is ready to use.

### Method 2: Manual Installation (Advanced Users)

**Step 1:** Locate Plugin Directory

The plugin directory location depends on your OS:

**Windows:**
```
%LOCALAPPDATA%\qBittorrent\nova3\engines\
```
Full path typically:
```
C:\Users\YourUsername\AppData\Local\qBittorrent\nova3\engines\
```

**Linux:**
```
~/.local/share/qBittorrent/nova3/engines/
```
Full path typically:
```
/home/yourusername/.local/share/qBittorrent/nova3/engines/
```

**macOS:**
```
~/Library/Application Support/qBittorrent/nova3/engines/
```

**Step 2:** Create Directory (if needed)

If the directory doesn't exist:

```bash
# Linux/macOS
mkdir -p ~/.local/share/qBittorrent/nova3/engines/

# Windows (PowerShell)
New-Item -Path "$env:LOCALAPPDATA\qBittorrent\nova3\engines\" -ItemType Directory -Force
```

**Step 3:** Copy Plugin File

```bash
# Linux/macOS
cp bitmagnet.py ~/.local/share/qBittorrent/nova3/engines/

# Windows (PowerShell)
Copy-Item bitmagnet.py "$env:LOCALAPPDATA\qBittorrent\nova3\engines\"
```

**Step 4:** Verify File

```bash
# Linux/macOS
ls -lh ~/.local/share/qBittorrent/nova3/engines/bitmagnet.py

# Windows (PowerShell)
Get-Item "$env:LOCALAPPDATA\qBittorrent\nova3\engines\bitmagnet.py"
```

**Step 5:** Restart qBittorrent

- Completely close qBittorrent (check system tray)
- Restart qBittorrent
- Open Search (F3)
- Enable "Bitmagnet" checkbox

### Method 3: Command Line Installation

**Linux/macOS:**
```bash
# Download and install in one command
curl -o ~/.local/share/qBittorrent/nova3/engines/bitmagnet.py \
  https://raw.githubusercontent.com/bitmagnet-io/bitmagnet-qbittorrent-search-plugin/main/bitmagnet.py
```

**Windows (PowerShell as Administrator):**
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/bitmagnet-io/bitmagnet-qbittorrent-search-plugin/main/bitmagnet.py" `
  -OutFile "$env:LOCALAPPDATA\qBittorrent\nova3\engines\bitmagnet.py"
```

## Post-Installation Configuration

### Default Configuration (Localhost)

The plugin works immediately if Bitmagnet is on `localhost:3333`.

First run creates `bitmagnet.json` with defaults:
```json
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

### Custom Configuration

**Step 1:** Locate config file

The config file is in the same directory as the plugin:
- **Windows**: `%LOCALAPPDATA%\qBittorrent\nova3\engines\bitmagnet.json`
- **Linux/macOS**: `~/.local/share/qBittorrent/nova3/engines/bitmagnet.json`

**Step 2:** Edit configuration

```bash
# Linux/macOS
nano ~/.local/share/qBittorrent/nova3/engines/bitmagnet.json

# Windows
notepad %LOCALAPPDATA%\qBittorrent\nova3\engines\bitmagnet.json
```

**Step 3:** Modify settings

Example for remote server:
```json
{
    "api_url": "http://192.168.1.50:3333/graphql",
    "base_url": "http://192.168.1.50:3333",
    "max_pages": 10,
    "results_per_page": 100
}
```

**Step 4:** Save and test

- Save the file
- No need to restart qBittorrent
- Next search will use new settings

## Verification

### Test the Plugin

**Via qBittorrent UI:**
1. Open Search (F3)
2. Check "Bitmagnet" box
3. Search for "ubuntu"
4. Results should appear within seconds

**Via Command Line:**
```bash
# Navigate to plugin directory
cd ~/.local/share/qBittorrent/nova3/engines/  # Linux/macOS
# or
cd %LOCALAPPDATA%\qBittorrent\nova3\engines\  # Windows

# Run test search
python3 nova2.py bitmagnet all "ubuntu"
```

Expected output (example):
```
magnet:?xt=urn:btih:ABC123...|ubuntu-22.04-desktop-amd64.iso|3.61 GB|150|25|http://localhost:3333|http://localhost:3333/#/torrents/ABC123...|-1
```

## Troubleshooting Installation

### Plugin Doesn't Appear in qBittorrent

**Possible Causes:**
- File not in correct directory
- Filename incorrect (must be `bitmagnet.py`)
- qBittorrent not restarted
- Python not in PATH

**Solutions:**
1. Verify file location:
   ```bash
   # Should exist
   ls ~/.local/share/qBittorrent/nova3/engines/bitmagnet.py
   ```

2. Check filename exactly `bitmagnet.py` (lowercase, .py extension)

3. Completely restart qBittorrent:
   - Close all windows
   - Check system tray for qBittorrent icon
   - Kill process if needed
   - Restart application

4. Verify Python installation:
   ```bash
   python3 --version
   which python3
   ```

### "Cannot Execute Plugin" Error

**Cause:** Python not found or wrong version

**Solution:**
1. Install Python 3.7+
2. Add Python to PATH
3. On Windows, reinstall Python with "Add to PATH" option checked

### Permission Denied

**Linux/macOS:**
```bash
chmod +x ~/.local/share/qBittorrent/nova3/engines/bitmagnet.py
```

**Windows:** Run qBittorrent as Administrator once

### Config File Not Created

**Manual Creation:**
```bash
# Create config file
cat > ~/.local/share/qBittorrent/nova3/engines/bitmagnet.json << 'EOF'
{
    "api_url": "http://localhost:3333/graphql",
    "base_url": "http://localhost:3333",
    "max_pages": 10,
    "results_per_page": 100
}
EOF
```

## Upgrading

### From Previous Version

1. Download new `bitmagnet.py`
2. Replace old file in plugin directory
3. Config file (`bitmagnet.json`) is preserved
4. Restart qBittorrent

### Automatic Update (if available)

qBittorrent may offer updates through the plugin manager:
1. Open **Search plugins...**
2. Click **Check for updates**
3. If update available, click **Update**

## Uninstallation

### Via qBittorrent UI

1. Open **Search plugins...**
2. Select "Bitmagnet"
3. Click **Uninstall**
4. Click **Yes** to confirm

### Manual Uninstallation

Delete the plugin files:

```bash
# Linux/macOS
rm ~/.local/share/qBittorrent/nova3/engines/bitmagnet.py
rm ~/.local/share/qBittorrent/nova3/engines/bitmagnet.json

# Windows (PowerShell)
Remove-Item "$env:LOCALAPPDATA\qBittorrent\nova3\engines\bitmagnet.py"
Remove-Item "$env:LOCALAPPDATA\qBittorrent\nova3\engines\bitmagnet.json"
```

## Next Steps

After installation:

1. 📖 Read [QUICKSTART.md](QUICKSTART.md) for usage guide
2. 🔧 Review [README.md](README.md) for advanced features
3. 💡 Check [examples/](examples/) for configuration templates
4. 🐛 Report issues on GitHub

## Support

- **Installation Help**: [GitHub Issues](https://github.com/bitmagnet-io/bitmagnet-qbittorrent-search-plugin/issues)
- **qBittorrent Forums**: [https://qbforums.shiki.hu/](https://qbforums.shiki.hu/)
- **Bitmagnet Docs**: [https://bitmagnet.io](https://bitmagnet.io)
