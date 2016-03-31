from stemming.porter2 import stem
import string
from dbn import DBN
import numpy as np

def create_dictionary(words):
    return dict((word, 0) for word in words)

def create_bag_of_words(dictionary, words):
    bow = create_dictionary(dictionary)
    for word in map(lambda w: stem(w), words):
        if word in bow:
            bow[word] += 1
    return bow

def load_dictionary(filepath):
    return open(filepath, "r").read().splitlines()

def calculate_hash(autoencoder_directory, bag_of_words):
    numpy_rng = np.random.RandomState(123)
    autoencoder = DBN.load_dbn_data(autoencoder_directory, numpy_rng)
    bow_array = np.asarray([bag_of_words.values()], dtype="float32")
    hash = autoencoder.propup_function(bow_array, is_autoencoder=True)
    return hash