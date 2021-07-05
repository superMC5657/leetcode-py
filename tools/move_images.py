# -*- coding: utf-8 -*-
# !@time: 2021/5/8 20 57
# !@author: superMC @email: 18758266469@163.com
# !@fileName: move_images.py

import os
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description='Move images script')
    parser.add_argument('jpeg_dir', default='', type=str)
    parser.add_argument('raf_dir', default='', type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    jpeg_dir = args.jpeg_dir
    raf_dir = args.raf_dir
    jpeg_list = [x[:-4] for x in os.listdir(jpeg_dir)]
    raf_list = os.listdir(raf_dir)
    for raf in raf_list:
        if raf[:-4] in jpeg_list:
            shutil.move(src=os.path.join(raf_dir, raf), dst=os.path.join(jpeg_dir, raf))
