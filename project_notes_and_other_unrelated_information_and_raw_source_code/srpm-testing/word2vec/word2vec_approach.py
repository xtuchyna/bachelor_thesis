import word2vec

#word2vec.word2phrase('../basicTesting/adult', './adult_phrased', verbose=True)

word2vec.word2vec('../basicTesting/adult_word2vec', './adult_vectorized.bin', size=10, verbose=True)

word2vec.word2clusters('../basicTesting/adult_word2vec', './adult_clusters.txt', 10, verbose=True)


