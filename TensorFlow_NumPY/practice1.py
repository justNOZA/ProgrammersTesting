import tensorflow as tf
import numpy as np

a = tf.constant(12)
sess = tf.Session()
print(sess.run(a))
b = tf.constant(35)
c = a + b
print(sess.run(c))
