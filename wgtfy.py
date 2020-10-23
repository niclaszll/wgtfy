#!/usr/bin/env python

import zipfile
import shutil
import os

zip_file_name = os.path.dirname(os.getcwd()) + ".zip"

# get files from directory
list_files = [f for f in os.listdir(".") if os.path.isfile(f)]

with zipfile.ZipFile(zip_file_name, "w") as zipF:
    for root, dirs, files in os.walk("."):
        for file in files:
            zipF.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)

# change file ext to .wgt
pre, ext = os.path.splitext(zip_file_name)

wgt_file = os.path.basename(os.getcwd()) + ".wgt"

# rename and move file
os.rename(zip_file_name, wgt_file)

# move file to correct directory
shutil.move(wgt_file, os.path.dirname(os.getcwd()))

print("Widget created successfully")
