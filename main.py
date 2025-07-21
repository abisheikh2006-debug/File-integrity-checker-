import os
import hashlib
import json

# Directory to check
CHECK_DIR = "your_directory_here"
# File to store known good hashes
HASH_FILE = "file_hashes.json"

def hash_file(path):
    hasher = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def create_hash_database():
    file_hashes = {}
    for root, _, files in os.walk(CHECK_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            file_hashes[full_path] = hash_file(full_path)
    with open(HASH_FILE, 'w') as f:
        json.dump(file_hashes, f, indent=2)
    print("✅ Hash database created.")

def check_integrity():
    if not os.path.exists(HASH_FILE):
        print("⚠️ Hash file not found. Please run create_hash_database() first.")
        return

    with open(HASH_FILE, 'r') as f:
        known_hashes = json.load(f)

    current_hashes = {}
    modified = []
    new_files = []
    deleted = []

    for root, _, files in os.walk(CHECK_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            current_hashes[full_path] = hash_file(full_path)

    for path, old_hash in known_hashes.items():
        if path not in current_hashes:
            deleted.append(path)
        elif old_hash != current_hashes[path]:
            modified.append(path)

    for path in current_hashes:
        if path not in known_hashes:
            new_files.append(path)

    print("🔍 Integrity Check Results:")
    if modified: print(f"✏️ Modified: {modified}")
    if new_files: print(f"🆕 New: {new_files}")
    if deleted: print(f"❌ Deleted: {deleted}")
    if not (modified or new_files or deleted): print("✅ No changes detected.")

# Uncomment below to run
# create_hash_database()
# check_integrity()
