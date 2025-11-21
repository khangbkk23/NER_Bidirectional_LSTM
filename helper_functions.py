import os
import shutil
import zipfile

def unzip(path, dest, delete=True):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Zip file does not exist: {path}")
    
    if not zipfile.is_zipfile(path):
        raise zipfile.BadZipFile(f"Not a valid zip file: {path}")
    
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(dest)
        print(f"Unzipped into: {dest}")
    if delete:
        os.remove(path)
    else:
        print(f"Do not remove zipfile.")
    
    return dest

def move_file(path: str, dest: str):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Source file does not exist: {path}")
    
    os.makedirs(dest, exist_ok=True)
    new_path = shutil.move(path, dest)
    return new_path
    