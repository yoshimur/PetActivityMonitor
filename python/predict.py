# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
import tensorflow as tf
from PIL import Image

import cnn as nn

if __name__ == '__main__':
    labels = []
    backup_dir = os.path.join(os.getcwd(), 'ckpt')

    f = open('images/label.txt', 'r')
    for line in f:
        labels.append(line.rstrip())

    test_image = []
    for i in range(1, len(sys.argv)):
        img = Image.open(sys.argv[i])
        img = img.resize((nn.IMAGE_SIZE, nn.IMAGE_SIZE))
        test_image.append(np.asarray(img) / 255.0)
    test_image = np.asarray(test_image)

    images_placeholder = tf.placeholder("float", shape=(None, nn.IMAGE_SIZE, nn.IMAGE_SIZE, 3))
    labels_placeholder = tf.placeholder('float', shape=(None, nn.NUM_CLASSES))
    keep_prob = tf.placeholder("float")

    logits = nn.inference(images_placeholder, keep_prob)
    sess = tf.InteractiveSession()

    saver = tf.train.Saver()
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, backup_dir + "/model.ckpt")

    for i in range(len(test_image)):
        pred = np.argmax(logits.eval(feed_dict={
            images_placeholder: [test_image[i]],
            keep_prob: 1.0})[0])
        print(labels[pred])

