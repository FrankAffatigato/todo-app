import zipfile
import pathlib

def mark_archive(filepaths, dest_dir, zip_name):
    if zip_name[-4:] != ".zip":
        zip_name = zip_name + ".zip"
    dest_dir = pathlib.Path(dest_dir, zip_name)
    with zipfile.ZipFile(dest_dir, "w") as archive:
        for filepath in filepaths:
            arcname = pathlib.Path(filepath).name
            archive.write(filepath, arcname=arcname)
