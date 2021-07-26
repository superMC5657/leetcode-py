import os
import sys
import shutil

args = sys.argv
root_dir = args[1]
target_dir = args[2]

for root, dirs, files in os.walk(root_dir):
    if root is root_dir:
        continue
    for d in files:
        src = os.path.join(root, d)
        trg = os.path.join(target_dir, d)
        shutil.move(src, trg)

