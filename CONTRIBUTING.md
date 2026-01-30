# Contributing to Bitmagnet qBittorrent Search Plugin

Thank you for your interest in contributing! This guide will help you get started.

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Use the bug report template
3. Include:
   - qBittorrent version
   - Python version
   - Bitmagnet version
   - Operating system
   - Error messages
   - Steps to reproduce

### Suggesting Features

1. Check existing feature requests
2. Describe the use case
3. Explain expected behavior
4. Consider backward compatibility

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Open a pull request

## Development Setup

### Prerequisites

- Python 3.7+
- qBittorrent 4.1.0+
- Bitmagnet instance for testing
- Git

### Testing

```bash
# Download test files
curl -O https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/nova2.py
curl -O https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/helpers.py
curl -O https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/novaprinter.py
curl -O https://raw.githubusercontent.com/qbittorrent/qBittorrent/master/src/searchengine/nova3/socks.py

# Run tests
python3 nova2.py bitmagnet all "test"
```

## Code Style

- Follow PEP 8
- Use type hints
- Add docstrings to functions
- Keep functions focused and small
- Comment complex logic

## Commit Messages

Format:
```
<type>: <subject>

<body>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Testing
- `chore`: Maintenance

Example:
```
feat: add support for custom timeout configuration

- Add timeout parameter to config
- Update documentation
- Add validation
```

## Questions?

Open an issue or discussion on GitHub.

Thank you for contributing!
