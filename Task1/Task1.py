import os
import shutil

def copy_folder(src_path, dest_path):
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Source folder '{src_path}' does not exist.")
    
    if not os.path.isdir(src_path):
        raise NotADirectoryError(f"Source path '{src_path}' is not a directory.")
    
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    for dirpath, dirnames, filenames in os.walk(src_path):
        relative_path = os.path.relpath(dirpath, src_path)
        dest_dir = os.path.join(dest_path, relative_path)
        os.makedirs(dest_dir, exist_ok=True)
        
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest_dir, filename)
            shutil.copy2(src_file, dest_file)
    
    print(f"Folder '{src_path}' has been copied to '{dest_path}' successfully.")

src_folder = input("Copy this path:")
dest_folder = input("Copy path to:")

try:
    copy_folder(src_folder, dest_folder)
except (FileNotFoundError, NotADirectoryError) as e:
    print(e)
