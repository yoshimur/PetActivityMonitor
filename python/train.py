# -*- coding: utf-8 -*-
import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import cnn as nn

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('train', os.path.join('images', 'train_data_file.txt'), 'File name of train data')
flags.DEFINE_string('test', os.path.join('images', 'test_data_file.txt'), 'File name of test data')
flags.DEFINE_string('train_dir', 'images/train_data', 'Directory to put the training data')
flags.DEFINE_integer('max_steps', 200, 'Number of steps to run trainer')
flags.DEFINE_integer('batch_size', 10, 'Batch size, must divide evenly into the data set sizes')
flags.DEFINE_float('learning_rate', 1e-5, 'Initial learning rate')

if __name__ == '__main__':
    # Initialize

    # prepare backup dir
    backup_dir = os.path.join(os.getcwd(), 'ckpt')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    train_image = []
    train_label = []

    f = open(os.path.join(os.getcwd(), FLAGS.train), 'r')
    for line in f:
        line = line.rstrip()
        l = line.split()
        img = Image.open(l[0])
        img = img.resize((nn.IMAGE_SIZE, nn.IMAGE_SIZE))
        train_image.append(np.asarray(img) / 255.0)
        tmp = np.zeros(nn.NUM_CLASSES)
        tmp[l[1]] = 1.0
        train_label.append(tmp)

    train_image = np.asarray(train_image)
    train_label = np.asarray(train_label)

    f.close()

    test_image = []
    test_label = []
    f = open(os.path.join(os.getcwd(), FLAGS.test), 'r')
    for line in f:
        line = line.rstrip()
        l = line.split()
        img = Image.open(l[0])
        img = img.resize((nn.IMAGE_SIZE, nn.IMAGE_SIZE))
        test_image.append(np.asarray(img) / 255.0)
        tmp = np.zeros(nn.NUM_CLASSES)
        tmp[l[1]] = 1.0
        test_label.append(tmp)

    test_image = np.asarray(test_image)
    test_label = np.asarray(test_label)

    start = time.time()

    with tf.Graph().as_default():
        images_placeholder = tf.placeholder("float", shape=(None, nn.IMAGE_SIZE, nn.IMAGE_SIZE, 3))
        labels_placeholder = tf.placeholder('float', shape=(None, nn.NUM_CLASSES))
        keep_prob = tf.placeholder("float")

        logits = nn.inference(images_placeholder, keep_prob)

        loss_value = nn.loss(logits, labels_placeholder)
        train_op = nn.training(loss_value, FLAGS.learning_rate)
        acc = nn.accuracy(logits, labels_placeholder)

        saver = tf.train.Saver()
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        summary_op = tf.summary.merge_all()
        summary_writer = tf.summary.FileWriter(FLAGS.train_dir, sess.graph)

        # train
        for step in range(FLAGS.max_steps):
            for i in range(int(len(train_image) / FLAGS.batch_size)):
                batch = FLAGS.batch_size * i
                print('batch #', i)

                op = sess.run(train_op,
                              feed_dict={images_placeholder: train_image[batch:batch + FLAGS.batch_size],
                                         labels_placeholder: train_label[batch:batch + FLAGS.batch_size],
                                         keep_prob: 0.5})

                train_accuracy = sess.run(acc,
                                          feed_dict={images_placeholder: train_image,
                                                     labels_placeholder: train_label,
                                                     keep_prob: 1.0})
                train_loss = sess.run(loss_value,
                                      feed_dict={images_placeholder: train_image,
                                                 labels_placeholder: train_label,
                                                 keep_prob: 1.0})

                print("Step %d, training accuracy %g loss %g" % (step, train_accuracy, train_loss))

                summary_str = sess.run(summary_op,
                                       feed_dict={images_placeholder: train_image,
                                                  labels_placeholder: train_label,
                                                  keep_prob: 1.0})

                summary_writer.add_summary(summary_str, step)

    elapsed_time = time.time() - start

    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("test accuracy %g" % sess.run(acc, feed_dict={
                images_placeholder: test_image,
                labels_placeholder: test_label,
                keep_prob: 1.0}))

    # save model
    save_path = saver.save(sess, backup_dir + "/model.ckpt")
