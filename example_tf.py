#!/bin/python3.9

'''
A simple tensorflow example
'''

import tensorflow as tf

print(tf.reduce_sum(tf.random.normal([1000, 1000])))