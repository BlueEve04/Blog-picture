import os
import logging
from PIL import Image

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def resize_image(image_path, max_size=512*1024):  # 调整最大文件大小为512KB
    initial_size = os.path.getsize(image_path)
    logging.info(f"Initial size of {image_path}: {initial_size} bytes")
    
    if initial_size <= max_size:
        logging.info(f"Skipping {image_path}, already under {max_size} bytes")
        return
    
    with Image.open(image_path) as img:
        img_format = img.format
        width, height = img.size
        while os.path.getsize(image_path) > max_size:
            width = int(width * 0.9)
            height = int(height * 0.9)
            img = img.resize((width, height), Image.LANCZOS)
            img.save(image_path, format=img_format, quality=85)
        final_size = os.path.getsize(image_path)
        logging.info(f"Resized and saved: {image_path}, new size: {final_size} bytes")

def process_directory(directory):
    logging.debug(f"Starting to process directory: {directory}")
    for root, _, files in os.walk(directory):
        logging.debug(f"Checking directory: {root}")
        for file in files:
            logging.debug(f"Found file: {file}")
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                image_path = os.path.join(root, file)
                logging.info(f"Processing: {image_path}")
                resize_image(image_path)
            else:
                logging.debug(f"Skipping non-image file: {file}")

if __name__ == "__main__":
    directory = "D:/000MyFiles/CodeScope/Blog-Pic/Blog-picture"
    logging.debug(f"Script started with directory: {directory}")
    process_directory(directory)
    logging.debug("Script finished")
