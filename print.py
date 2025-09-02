import os

def get_project_source_code(root_dir='.', output_filename='project_source_code.txt'):
    """
    Traverses a directory and returns a dictionary of all source code files,
    excluding the node_modules directory and the output file itself.
    """
    project_files = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude the node_modules directory from traversal
        if 'venv' in dirnames:
            dirnames.remove('venv')

        for filename in filenames:
            # Skip the output file to prevent it from including itself
            if filename == output_filename:
                continue
            if filename == 'package-lock.json':
                continue

            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Use the file path relative to the root_dir as the key
                    relative_path = os.path.relpath(file_path, root_dir)
                    project_files[relative_path] = content
            except Exception as e:
                # Handle files that cannot be read (e.g., binary files)
                print(f"Could not read file {file_path}: {e}")
                
    return project_files

def save_to_file(source_code_dict, output_filename='project_source_code.txt'):
    """
    Writes the content of all source code files to a single text file.
    Each file's content is preceded by its file path.
    """
    with open(output_filename, 'w', encoding='utf-8') as f:
        for file_path, content in source_code_dict.items():
            f.write(f"--- File: {file_path} ---\n")
            f.write(content)
            f.write("\n\n")
    print(f"All source code has been saved to '{output_filename}'")

if __name__ == "__main__":
    output_file_name = 'project_source_code.txt'
    # Get all source code files, excluding the output file
    all_source_code = get_project_source_code(output_filename=output_file_name)
    
    # Save all the source code to a single text file
    save_to_file(all_source_code, output_filename=output_file_name)