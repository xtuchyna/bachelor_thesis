import gensim

model = gensim.models.Word2Vec.load('dependencies_recommender_w2v_model')

print(model.wv.most_similar(positive=['libstdc++']))


for line in model.predict_output_word(['libstdc++'], topn=10):
    print(line)

print('others:')

for line in model.predict_output_word(['alleyoop', 'dfhack', 'valkyrie', 'valgrind-devel'], topn=100):
    print(line)


