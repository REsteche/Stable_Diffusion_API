import os
import shutil

def cleanup(file_path):
    try:
        dir, _ = file_path.split("/")
        shutil.rmtree(dir)
    except Exception as error:
        print(error)
        os.remove(file_path)
    