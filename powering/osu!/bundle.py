from os import path, replace
from shutil import make_archive

DIR = path.dirname(path.realpath(__file__))
DST = path.join(DIR, f"{path.basename(DIR)}")
SRC = path.join(DIR, "dist")

make_archive(DST, "zip", SRC)
replace(f"{DST}.zip", f"{DST}.osk")