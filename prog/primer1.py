#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# написать программу, которая позволяет перемещать все текстовые файлы в один каталог.

import glob
import os
import shutil

if __name__ == "__main__":
    for file_name in glob.glob("*.txt"):
        new_path = os.path.join("archive", file_name)
        shutil.move(file_name, new_path)
