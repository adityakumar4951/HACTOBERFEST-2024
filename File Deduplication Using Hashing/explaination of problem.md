This is program that identifies duplicate files based on their content. The program should compute a hash for each file, and if two or more files have the same hash, they are considered duplicates. The program should remove the duplicates, keeping only one instance of each.
In file systems, duplicate files can accumulate over time, consuming storage space. This program uses hashing (SHA-256) to generate a unique hash for the content of each file. By comparing the hashes, the program identifies duplicates and removes them, freeing up space.

Edge Cases:
1. Files that do not exist.
2. Empty files that are valid but should be considered in the deduplication process.
3. Handling large files by reading them in chunks to avoid memory issues.

Test Cases:
Input: ["file1.txt", "file2.txt", "file3.txt", "nonexistent.txt"]
Output: Unique files with hash comparison, and error for non-existent file.

Key Features:
1. Uses hashing to detect duplicate files.
2. Focuses on efficient file reading and hash computation.
3. Real-world application in cloud storage or backup systems.