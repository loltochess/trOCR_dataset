import os
from tqdm import tqdm

source_folders = ['valid_background','valid_basic','valid_blur_1','valid_blur_2']

# 대상 폴더
destination_folder = 'valid'

# 대상 폴더가 없다면 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

dest_path=os.path.join(os.getcwd(),destination_folder)

for src in source_folders:
    source_path=os.path.join(os.getcwd(), src)
    files = os.listdir(source_path)
    for f in tqdm(files, desc=f"Moving files from {src}"):
        if f.endswith(".jpg"):
            src_file_path = os.path.join(source_path, f)
            dest_file_path = os.path.join(dest_path, f)
            os.rename(src_file_path, dest_file_path)