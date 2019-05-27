import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb as imdb
import numpy as np


def main():
    version_print()
    # num_words=x keeps the x most frequently used words
    # the other rare ones are excluded
    #
    # index_from=x tells us how to index dictionary - see the reason
    # for number 2 in review_example()
    #
    # everything described here https://keras.io/datasets/
    (train_data, train_labels), (test_data, test_labels) = imdb.load_data(
                                                            num_words=10000,
                                                            index_from=2)

    dataset_print(train_data, train_labels)
   
    review_example(train_data[7])


def review_example(review):
    word_index = imdb.get_word_index()

    # The index_from 
    word_index = {k:(v+2) for k,v in word_index.items()} 
    word_index["<PAD>"] = 0
    # used as an indication for the beginning of each review 
    word_index["<START>"] = 1
    # unknown, depends on how many num_words we have specified in num_words
    # the bigger the number the less occurences of <UNK> will text have
    word_index["<UNK>"] = 2
    

    word_index_inverted = {v:k for k,v in word_index.items()}
    print(' '.join([word_index_inverted.get(i) for i in review]))

def dataset_print(dataset_data, dataset_labels):
    print("number of reviews: ", len(dataset_data))
    print("number of labels: ", len(dataset_labels))
    print("example of random review: ")


def version_print():
    print("tensorflow version: ", tf.__version__)
    print("keras version: ", keras.__version__)
    print("numpy version: ", np.__version__)
    print("\n\n")


if __name__ == "__main__":
    main()
