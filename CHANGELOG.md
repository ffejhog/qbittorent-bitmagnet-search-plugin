# Changelog

All notable changes to the Bitmagnet qBittorrent Search Plugin will be documented in this file.

## [1.2] - 2024-01-30

### Added
- **Unknown Category Support**: Added non-standard `unknown` category for unclassified content
  - Available via command line: `python nova2.py bitmagnet unknown "search term"`
  - Not visible in qBittorrent UI dropdown (non-standard category limitation)
  - Returns ALL content (no filter) - same as 'all' category

### Changed
- **IMPORTANT**: 'all' category now includes xxx content and unclassified torrents
  - Changed from filtered list to no filter (None)
  - Now searches everything in Bitmagnet without restrictions
  - Ensures unclassified torrents are included in searches
- Updated documentation to reflect new behavior

### Technical Details
- Changed `CATEGORY_MAP['all']` from list of types to `None` (no filter)
- Added `'unknown': '10'` to `supported_categories`
- Added `'unknown': None` to `CATEGORY_MAP`
- Updated search logic to handle `None` (no filter) properly

## [1.1] - 2024-01-30

### Added
- **XXX Category Support**: Added non-standard `xxx` category for adult content
  - Available via command line: `python nova2.py bitmagnet xxx "search term"`
  - Not visible in qBittorrent UI dropdown (non-standard category limitation)
  - Initially excluded from "All" category searches (changed in v1.2)
  - Maps to Bitmagnet's `xxx` content type

### Changed
- Updated documentation to explain xxx category usage and limitations
- Added examples for xxx category searches in guides

### Technical Details
- Added `'xxx': '9'` to `supported_categories`
- Added `'xxx': ['xxx']` to `CATEGORY_MAP`

## [1.0] - 2024-01-30

### Initial Release
- GraphQL API integration with Bitmagnet
- Support for 9 standard qBittorrent categories (all, movies, tv, anime, music, books, games, software, pictures)
- JSON configuration system
- Pagination support
- Category filtering
- Error handling
- Comprehensive documentation
- MIT License
