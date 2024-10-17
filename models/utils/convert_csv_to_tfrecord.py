import csv
import tensorflow as tf


# Path to your CSV file containing image paths and breed names
csv_file_path = 'models/data/dog_breeds.csv'

# TFRecord file to write the data to
tfrecord_file_path = 'models/data/dog_breeds.tfrecord'

def _bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value.encode()]))

def csv_to_tfexample(image_path, breed_name):
    """Converts image path and breed name to tf.train.Example"""
    return tf.train.Example(features=tf.train.Features(feature={
        'image_path': _bytes_feature(image_path),
        'breed_name': _bytes_feature(breed_name),
    }))



# Open the CSV file and write to TFRecord
with tf.io.TFRecordWriter(tfrecord_file_path) as writer:
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            image_path, breed_name = row  # Assuming your CSV has two columns: image_path and breed_name
            
            # Convert to tf.train.Example
            tf_example = csv_to_tfexample(image_path, breed_name)
            
            # Write the serialized example to TFRecord
            writer.write(tf_example.SerializeToString())
