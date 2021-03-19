import numpy as np
from tensorflow.keras.utils import to_categorical
from scipy.signal import convolve2d


def smooth_by_neighbours(labels, kernel, n_classes):
    kernel = np.array(kernel).reshape(-1, 1)
    one_hot_labels = to_categorical(labels, n_classes)
    return convolve2d(one_hot_labels,
                      kernel,
                      mode="same", boundary='symm')


def smoothen(one_hot_labels, max_alpha, n_classes):
    alpha = np.random.rand() * max_alpha
    return (1-alpha) * one_hot_labels + (alpha/n_classes)


# kernel = [0.1, 0.8, 0.1]
# labels = np.random.randint(0, 5, 10)
# s1 = smooth_by_neighbours(labels, kernel, 5)
# s2 = smoothen(s1, 0.1, 5)