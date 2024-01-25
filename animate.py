import re
import os
from os import path

ANIMATED_EXPORT_RE = re.compile("^[a-z0-9-]+@2x[0-9]+.png$")
DIR = path.join(path.dirname(path.realpath(__file__)), "dist")

def resolve_index(index: str):
    index = index.lstrip("0")

    return "0" if len(index) == 0 else index

for root, dirs, files in os.walk(DIR):
    for file in files:
        if not ANIMATED_EXPORT_RE.match(file):
            continue

        name, index = file.removesuffix(".png").split("@2x")

        os.replace(path.join(root, file), path.join(root, f"{name}-{resolve_index(index)}@2x.png"))