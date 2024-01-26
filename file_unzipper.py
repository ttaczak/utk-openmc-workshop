import zipfile as zf
files = zf.ZipFile("utk-openmc-workshop-main.zip", 'r')
files.extractall()
files.close()