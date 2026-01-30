# Version 1.2 Update Summary

## 🎯 Key Changes

### ✅ All Category Now Includes Everything
The `all` category no longer filters by content type:
- **Before (v1.1)**: Filtered to specific types, excluding xxx and unclassified
- **After (v1.2)**: No filter - includes ALL content (classified + unclassified + xxx)

### ✅ New Unknown Category Added
Added `unknown` as a non-standard category:
- Same behavior as `all` (no filter)
- Useful for searching absolutely everything
- Command line only: `python nova2.py bitmagnet unknown "query"`

## 📊 Category Behavior Matrix

| Category | Filter Applied | Includes XXX? | Includes Unclassified? | Available In UI? |
|----------|---------------|---------------|----------------------|------------------|
| all | None (no filter) | ✅ Yes | ✅ Yes | ✅ Yes |
| movies | movie | ❌ No | ❌ No | ✅ Yes |
| tv | tv_show | ❌ No | ❌ No | ✅ Yes |
| anime | tv_show | ❌ No | ❌ No | ✅ Yes |
| music | music | ❌ No | ❌ No | ✅ Yes |
| books | ebook, comic, audiobook | ❌ No | ❌ No | ✅ Yes |
| games | game | ❌ No | ❌ No | ✅ Yes |
| software | software | ❌ No | ❌ No | ✅ Yes |
| pictures | (empty) | ❌ No | ❌ No | ✅ Yes |
| xxx | xxx | ✅ Only xxx | ❌ No | ❌ No (CLI only) |
| unknown | None (no filter) | ✅ Yes | ✅ Yes | ❌ No (CLI only) |

## 🔧 Technical Changes

### Code Changes
```python
# Version 1.1 (Old)
CATEGORY_MAP = {
    'all': ['movie', 'tv_show', 'music', 'ebook', 'comic', 'audiobook', 'game', 'software'],
    'xxx': ['xxx'],
}

# Version 1.2 (New)
CATEGORY_MAP = {
    'all': None,  # No filter = everything
    'xxx': ['xxx'],
    'unknown': None,  # Same as 'all'
}
```

### Search Logic Updates
```python
# Now handles None properly
if content_types is not None and len(content_types) == 0:
    return  # Only return early for empty list (pictures)
# None means no filter - search everything
```

### Categories Added
- `'unknown': '10'` in `supported_categories`
- `'unknown': None` in `CATEGORY_MAP`

## 📝 Rationale

### Why Include XXX in All?
1. User requested it: "If all returns xxx as well that's fine"
2. Simpler behavior: No special exclusion logic needed
3. Matches Bitmagnet's behavior: No filter means truly everything
4. Users who don't want xxx can use specific categories

### Why Add Unknown Category?
1. **Unclassified torrents exist**: Many torrents don't have a content type
2. **Previous 'all' missed them**: Filtering by types excluded unclassified content
3. **Discovery**: Users can now find all unclassified torrents
4. **Completeness**: Ensures comprehensive search coverage

## 🚀 User Impact

### For Standard Users (qBittorrent UI)
- Searching "All" now returns more results (includes xxx + unclassified)
- May see adult content in "All" searches
- Can use specific categories (Movies, TV, etc.) to avoid xxx

### For Advanced Users (Command Line)
- New `unknown` category available
- Both `all` and `unknown` search everything
- Can filter to xxx-only with `xxx` category

## 📋 Migration Guide

### If Users Want to Avoid XXX in "All"
They should use individual categories instead:
```bash
# Instead of searching "all"
python nova2.py bitmagnet all "query"

# Use specific categories
python nova2.py bitmagnet movies "query"
python nova2.py bitmagnet tv "query"
# etc.
```

### If Users Want Only Unclassified
Use the `unknown` category (same as `all` now):
```bash
python nova2.py bitmagnet unknown "query"
```

## ✅ Testing Checklist

- [ ] `all` category returns xxx content
- [ ] `all` category returns unclassified torrents
- [ ] `unknown` category returns same results as `all`
- [ ] `xxx` category returns only xxx content
- [ ] Specific categories (movies, tv, etc.) still filter correctly
- [ ] Pictures category returns no results (empty filter)

## 📚 Documentation Updated

1. ✅ README.md - Updated category table and notes
2. ✅ QUICKSTART.md - Added unknown category example
3. ✅ PROJECT_SUMMARY.md - Updated category matrix
4. ✅ CHANGELOG.md - Documented breaking change
5. ✅ bitmagnet.py - Updated to v1.2

## 🎓 Version History

- **v1.0**: Initial release (9 standard categories)
- **v1.1**: Added xxx category (excluded from all)
- **v1.2**: All includes everything + added unknown category

---

**Current Version**: 1.2
**Plugin Categories**: 11 total (9 standard + 2 non-standard)
**Breaking Change**: Yes (all category behavior changed)
