#!/usr/bin/env python

import zipfile
import os

zip_file_name = os.path.basename(os.getcwd()) + ".zip"

# get files from directory
list_files = [f for f in os.listdir(".") if os.path.isfile(f)]

# zip files
with zipfile.ZipFile(zip_file_name, "w") as zipF:
    for file in list_files:
        zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)

# change file ext to .wgt
pre, ext = os.path.splitext(zip_file_name)
os.rename(zip_file_name, pre + ".wgt")

print("Widget created successfully")

