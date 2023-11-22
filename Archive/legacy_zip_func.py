import zipfile
import os

def compress_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        # Add the file to the zip archive
        zipf.write(file_path, arcname=os.path.basename(file_path))

# Specify the file to compress and the zip file path
file_to_compress = r'C:\Users\ifran\OneDrive\Desktop\text.txt'  # Update this path to a valid file
zip_file_path = r'C:\Users\ifran\OneDrive\Desktop\text.zip'  # Update this path

# Compress the file
compress_file(file_to_compress, zip_file_path)