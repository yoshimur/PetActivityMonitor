# -*- coding: utf-8 -*-

import csv
import os

folderlist = os.listdir()

for folder in folderlist:
    print('target directory is %s' % folder)
