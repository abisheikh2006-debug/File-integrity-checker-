# File Integrity Checker

This is a basic Python-based File Integrity Checker developed as part of a cybersecurity and ethical hacking internship.

## Features
- Creates SHA-256 hash of each file in a directory
- Detects any changes (modifications, deletions, or additions)

## Usage
1. Set `CHECK_DIR` in `main.py` to the directory you want to monitor.
2. Run `create_hash_database()` to save the current file hashes.
3. Later, run `check_integrity()` to detect any changes.

## Example
```bash
python main.py
```
