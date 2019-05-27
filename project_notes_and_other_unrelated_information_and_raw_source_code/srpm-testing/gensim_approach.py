import gensim
from os import listdir
from os.path import isfile, join
from sklearn import preprocessing

path = '../basicTesting/'
file_lst = [f for f in listdir(path) if isfile(join(path, f))]

entries = []
max_size = 0

for x in file_lst:
	cur_entry = []
	with open(join(path,x)) as file:
            cur_entry = [line.rstrip('\n') for line in file]
            cur_entry = [dependency.split()[0] for dependency in cur_entry]
            max_size = len(cur_entry) if len(cur_entry) > max_size else max_size

	entries.append(cur_entry)
print("dependencies from ", path, "were successfully extracted")
print("dependencies contain: ", len(list(x for y in entries for x in y)))
print("maximal transaction size: ", max_size)

trans = entries

model = gensim.models.Word2Vec(
        trans,
        size=300,
        window=max_size*2,
        min_count=1,
        workers=10,
        sg=0,
        cbow_mean=0)
model.train(trans, total_examples=len(trans), epochs=50)

print(model.wv.most_similar(positive=['bread']))
print(model.predict_output_word(['green', 'yellow'], topn=10))

print('saving the model')
model.save('dependencies_recommender_w2v_model')

