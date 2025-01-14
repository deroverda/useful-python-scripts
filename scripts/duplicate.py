import os
import hashlib

def get_file_hash(file_path, hash_algo='sha256'):
    """Calculate the hash of a file using the specified algorithm."""
    hash_function = hashlib.new(hash_algo)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_function.update(chunk)
    return hash_function.hexdigest()

def find_duplicate_files(directory, hash_algo='sha256'):
    """Find duplicate files in the specified directory by checking their hashes."""
    file_hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = get_file_hash(file_path, hash_algo)
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                else:
                    file_hashes[file_hash] = file_path
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                continue

    return duplicates

def display_duplicates(duplicates):
    """Display the list of duplicate files."""
    if duplicates:
        print("Duplicate files found:")
        for original, duplicate in duplicates:
            print(f"Original: {original}\nDuplicate: {duplicate}\n")
    else:
        print("No duplicate files found.")

def main():
    # Get the directory from the user
    directory = input("Enter the directory to scan for duplicates: ").strip()
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # Find and display duplicates
    duplicates = find_duplicate_files(directory)
    display_duplicates(duplicates)

if __name__ == "__main__":
    main()
