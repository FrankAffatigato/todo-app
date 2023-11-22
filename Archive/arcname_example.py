import pathlib
filepath = "c:user/desktop/file"
arcname = pathlib.Path(filepath).name
print(arcname)