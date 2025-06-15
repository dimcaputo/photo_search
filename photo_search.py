import os
import sys
from PIL import Image

def write_list_to_txt(list_to_save:list, filename:str):
    with open(f'{filename}.txt', 'w') as f:
        for item in list_to_save:
            f.write(item)
            f.write('\n')


def get_img_paths(drive_path:str) -> (list, list):
    list_img_paths = []
    list_errors = []
    formats = ('.jpg', '.jpeg', '.png', '.tiff', '.raw', '.heif', '.dng', '.bmp', '.webp', '.psd')
    for root, dirs, files in os.walk(drive_path):
        for file in files:
            full_path = os.path.join(root,file)
            try:
                if not file.startswith('.') and file.endswith(formats):
                    list_img_paths.append(full_path)
            except:
                list_errors.append(full_path)
    return list_img_paths, list_errors

def get_valid_paths(list_img_paths:list) -> (list, list, list):
    list_valid_paths = []
    list_rejected_paths = []
    list_errors = []
    for path in list_img_paths:
        try:
            with Image.open(path, 'r') as im:
                width, height = im.size
                if 9/21 <= width/height <= 21/9:
                    list_valid_paths.append(path)
                else:
                    list_rejected_paths.append(path)
        except:
            list_errors.append(path)
    return list_valid_paths, list_rejected_paths, list_errors

