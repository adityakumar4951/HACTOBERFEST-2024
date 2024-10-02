import hashlib
import os

def hash_file(filepath):
    """Generate SHA-256 hash for a given file."""
    try:
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"File not found: {filepath}")
        return None

def remove_duplicates(file_paths):
    """Remove duplicate files based on hash comparison."""
    hash_set = set()
    unique_files = []
    
    for file in file_paths:
        file_hash = hash_file(file)
        if file_hash and file_hash not in hash_set:
            hash_set.add(file_hash)
            unique_files.append(file)
    
    return unique_files

# Test Cases
# Assuming you have files: "file1.txt", "file2.txt", "file3.txt" with different or identical content

file_paths = ["file1.txt", "file2.txt", "file3.txt", "nonexistent.txt"]
unique_files = remove_duplicates(file_paths)

# Expected Output: Unique files with hash comparison, should skip "nonexistent.txt" and print an error message.
print("Unique Files:", unique_files)
