__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import time
import zipfile
# opdr 1
def clean_cache():
    dir_path = './cache'
    if os.path.isdir('./cache'):
        shutil.rmtree(dir_path) #delete folder/cache
        os.mkdir(dir_path) #create folder/cache
        print(f"successfully cleared folder {dir_path[1:]}")
    else:
        os.mkdir(dir_path) #create folder/cache
        print(f"successfully cleared folder {dir_path[1:]}")
    return

#opdr 2

def cache_zip(file_path: str, cache_dir_path: str):
    clean_cache()
    wait(3)
    from zipfile import ZipFile
    ZipFile(file_path).extractall(cache_dir_path)
    print("files unzipped - ready Files include:")
    return

def wait(seconds):
    print(f"waiting {seconds} seconds for Windows to realize internal operations...")
    time.sleep(seconds)
    return

cache_zip("data.zip", "cache")

#opdr 3
def cached_files():
    path = os.path.abspath("cache")
    file_list = [entry.path for entry in os.scandir(path) if entry.is_file()]
    return file_list
    
print(cached_files())

# opdr 4

def find_password(cached_files):
    for i in cached_files:
        with open(i) as fp:
            line = fp.readline()
            while line:
                if "password" in line:
                    signal = line
                    file_number = i
                else:
                    pass
                line = fp.readline()     
                
    print(f'{signal} is in file: {file_number}')
    password_string = signal.replace("password: ", "")
    new_password_string = password_string.replace("\n", "")
    return new_password_string

print(find_password(cached_files()))