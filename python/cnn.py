# -*- coding: utf-8 -*-
import tensorflow as tf

NUM_CLASSES = 4

# IMAGE_SIZE can be multiplied by 4
IMAGE_SIZE = 64
IMAGE_PIXELS = IMAGE_SIZE * IMAGE_SIZE * 3
FC_LAYER_SIZE = int(IMAGE_SIZE / 2 / 2)


def inference(images_placeholder, keep_prob):

    def weight_variable(shape):
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(shape):
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    def conv2d(x, w):
        return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#   x_image = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, 3])
    x_image = images_placeholder

    with tf.name_scope('conv1') as scope:
        w_conv1 = weight_variable([5, 5, 3, 32])
        b_conv1 = bias_variable([32])
        h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)

    with tf.name_scope('pool1') as scope:
        h_pool1 = max_pool_2x2(h_conv1)

    with tf.name_scope('conv2') as scope:
        w_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])
        h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)

    with tf.name_scope('pool2') as scope:
        h_pool2 = max_pool_2x2(h_conv2)

    with tf.name_scope('fc1') as scope:
        w_fc1 = weight_variable([FC_LAYER_SIZE * FC_LAYER_SIZE * 64, 1024])
        b_fc1 = bias_variable([1024])
        h_pool2_flat = tf.reshape(h_pool2, [-1, FC_LAYER_SIZE * FC_LAYER_SIZE * 64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    with tf.name_scope('fc2') as scope:
        w_fc2 = weight_variable([1024, NUM_CLASSES])
        b_fc2 = bias_variable([NUM_CLASSES])

    with tf.name_scope('softmax') as scope:
        y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2) + b_fc2)
        # y_conv = tf.nn.softmax(tf.matmul(h_fc1, w_fc2) + b_fc2)
    return y_conv


def loss(logits, labels):
    delta = 1e-7
    cross_entropy = -tf.reduce_sum(labels * tf.log(logits + delta))
    tf.summary.scalar("cross_entropy", cross_entropy)
    return cross_entropy


def training(loss, learning_rate):
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)
    return train_step


def accuracy(logits, labels):
    correct_prediction= tf.equal(tf.argmax(logits, 1), tf.argmax(labels, 1))
    accurary = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    tf.summary.scalar('accuracy', accurary)
    return accurary
