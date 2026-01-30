# Update Summary - XXX Category Support Added

## Changes Made

### ✅ Added XXX Category Support (Version 1.1)

The plugin now includes a **non-standard `xxx` category** for adult content searches:

```python
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
    'xxx': '9',  # NEW: Non-standard category
}

CATEGORY_MAP = {
    'all': [...],  # xxx excluded for safety
    ...
    'xxx': ['xxx'],  # NEW: Adult content mapping
}
```

## How It Works

### ✅ For Advanced Users (Command Line)
Users can search adult content via command line:
```bash
python3 nova2.py bitmagnet xxx "search term"
```

### ⚠️ Limitation: Not in qBittorrent UI
- qBittorrent UI only shows the **9 standard categories** in its dropdown
- The `xxx` category is **non-standard** and won't appear in the UI
- This is a qBittorrent limitation, not a plugin issue

### 🔒 Safety: Excluded from "All"
- Searching "All" category **still excludes** xxx content
- Adult content is **opt-in only** - you must explicitly request it
- This prevents accidental exposure to adult content

## Updated Files

1. ✅ **bitmagnet.py** - Added xxx category and mapping
2. ✅ **README.md** - Documented xxx category with warnings
3. ✅ **QUICKSTART.md** - Added xxx search example
4. ✅ **PROJECT_SUMMARY.md** - Updated category table
5. ✅ **CHANGELOG.md** - NEW: Created changelog file

## Version Bump

- **Previous**: 1.0
- **Current**: 1.1

## Usage Examples

### Command Line
```bash
# Standard categories (work in UI and CLI)
python3 nova2.py bitmagnet all "ubuntu"
python3 nova2.py bitmagnet movies "the matrix"

# XXX category (CLI only - not in UI dropdown)
python3 nova2.py bitmagnet xxx "search term"
```

### In qBittorrent UI
Users will see these categories in the dropdown:
- ✅ All
- ✅ Anime
- ✅ Books
- ✅ Games
- ✅ Movies
- ✅ Music
- ✅ Pictures
- ✅ Software
- ✅ TV
- ❌ XXX (not visible - command line only)

## Why This Approach?

### Pros
- ✅ Adult content is accessible for those who want it
- ✅ Excluded from "All" searches (safer default)
- ✅ Opt-in approach (explicit request required)
- ✅ Works within qBittorrent's limitations

### Cons
- ⚠️ Not visible in qBittorrent UI dropdown
- ⚠️ Requires command line for xxx searches
- ℹ️ Users might not discover this feature

### Alternative Considered (Not Implemented)
**Including xxx in "all" searches** would have:
- ❌ Exposed users to adult content unexpectedly
- ❌ No way to opt-out
- ❌ Poor user experience

## Documentation Updates

All guides now include:
- Warning that xxx is non-standard
- Explanation of CLI-only limitation
- Examples of xxx category usage
- Safety notes about exclusion from "all"

## Testing

To test the xxx category:
```bash
cd ~/.local/share/qBittorrent/nova3/engines/
python3 nova2.py bitmagnet xxx "test query"
```

Expected: Returns results filtered to xxx content type from Bitmagnet.

## Backward Compatibility

✅ **Fully backward compatible**
- Existing searches unchanged
- "All" category behavior unchanged
- No breaking changes

## Summary

The plugin now supports **10 total categories**:
- 9 standard (visible in qBittorrent UI)
- 1 non-standard (command line only)

Adult content is accessible but requires **explicit opt-in** via the xxx category, maintaining safety while providing flexibility.
