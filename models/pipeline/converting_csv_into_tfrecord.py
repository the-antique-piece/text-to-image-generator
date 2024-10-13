import csv
import tensorflow as tf
import os


def _bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    if isinstance(value, type(tf.constant(0))):  # if value is a tensor
        value = value.numpy()  # get the numpy value of the tensor
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _int64_feature(value):
    """Returns an int64_list from an int / bool."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _float_feature(value):
    """Returns a float_list from a float."""
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def image_to_tfexample(image_string, label):
    """Converts image and label to tf.train.Example"""
    return tf.train.Example(features=tf.train.Features(feature={
        'image': _bytes_feature(image_string),
        'label': _int64_feature(label),
    }))