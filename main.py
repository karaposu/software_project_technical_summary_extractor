import os
import sys

def print_tree(directory, depth, max_depth, prefix=""):
    """Recursively prints the tree structure of the given directory up to a maximum depth."""
    if depth > max_depth:
        return

    if prefix == "":  # If this is the top-level call, print the directory itself
        print(directory)
    
    files = sorted(os.listdir(directory))
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = i == (len(files) - 1)  # Check if this file is the last in the list
        print(prefix + ("└── " if is_last else "├── ") + file)
        if os.path.isdir(path):  # If this is a directory, recurse into it with increased depth
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, depth+1, max_depth, new_prefix)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python tree.py [directory] [optional: max_depth]")
        sys.exit(1)
    
    root_directory = sys.argv[1]
    if not os.path.isdir(root_directory):
        print("Error: Directory does not exist.")
        sys.exit(1)
    
    # Default max_depth to a large number if not specified
    max_depth = int(sys.argv[2]) if len(sys.argv) == 3 else float('inf')
    
    print_tree(root_directory, 0, max_depth)

