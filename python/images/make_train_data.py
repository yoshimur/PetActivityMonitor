# -*- coding: utf-8 -*-
import os

cwd = os.getcwd()

train_data_dir = 'trains'
train = open(os.path.join(cwd, 'train_data_file.txt'), 'w')

folderlist = os.listdir(train_data_dir)
folderlist.sort()
i = 0
trainFolder = os.path.join(cwd, train_data_dir)
for folder in folderlist:
    targetFolder = os.path.join(trainFolder, folder)
    print('target directory is %s' % targetFolder)
    filelist = os.listdir(targetFolder)
    for file in filelist:
        print('File name: %s ' % file)
        filepath = os.path.join(trainFolder, folder, file)

        train.write('%s %d\n' % (filepath, i))

    i = i + 1

train.close()

# test data set
test_data_dir = 'test'
test = open(os.path.join(cwd, 'test_data_file.txt'), 'w')

folderlist = os.listdir(test_data_dir)
folderlist.sort()
i = 0
testFolder = os.path.join(cwd, test_data_dir)
for folder in folderlist:
    targetFolder = os.path.join(testFolder, folder)
    print('target directory is %s' % targetFolder)
    filelist = os.listdir(targetFolder)
    for file in filelist:
        print('File name: %s ' % file)
        filepath = os.path.join(testFolder, folder, file)

        test.write('%s %d\n' % (filepath, i))

    i = i + 1

test.close()

# label data set
labeltext = open(os.path.join(cwd, 'label.txt'), 'w')
folderlist = os.listdir(train_data_dir)
folderlist.sort()
for line in folderlist:
    labeltext.write(line + "\n")
labeltext.close()