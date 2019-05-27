
from os import listdir
from os.path import isfile, join
from sklearn import preprocessing

from apyori import apriori
import pyfpgrowth
#from fp_growth import find_frequent_itemsets

path = './basicTesting/'
file_lst = [f for f in listdir(path) if isfile(join(path, f))]

entries = []

for x in file_lst:
	cur_entry = []
	with open(join(path,x)) as file:
            cur_entry = [line.rstrip('\n') for line in file]
            cur_entry = [dependency.split()[0] for dependency in cur_entry]
	entries.append(cur_entry)
print("dependencies from ", path, "were successfully extracted")
print("dependencies contain: ", len(list(x for y in entries for x in y)))

# this was before, but encoder fits everything
# no need for unnecessary set conversion
# TODO: maybe compare the speed of this version with current
unique_vals = set(x for y in entries for x in y)
print("set contains: ", len(unique_vals))

encoder = preprocessing.LabelEncoder()
encoder.fit([x for y in entries for x in y])

# bound with unique_vals
# print('unique items:', len(unique_vals))
# print('full sum of items:', len(list(x for y in entries for x in y)))

labeled_entries = [encoder.transform(entry) for entry in entries]
print("labeling has ended")

#assert len(labeled_entries) == len(entries), "labeling of the entries failed"
#for x,y in zip(entries, labeled_entries):
#assert len(x) == len(y), "labeling of the entries failed"
print("labeling assertions ended")

# fp-growth approach 
#patterns = pyfpgrowth.find_frequent_patterns(labeled_entries, 0.2)
#print(patterns)
#rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
#print(rules)
#for rule in rules:
#    print(tuple(encoder.inverse_transform(rule)), encoder.inverse_transform(rules[rule][0]))
#    rules[tuple(encoder.inverse_transform(rule))] = rules.pop(rule)

print("apriori begins.....")
# apriori approach
occurence = 50
support_num = occurence / len(entries)
print("probability that item occurs", occurence, " times in dataset: ", support_num)
print("this probability will be used as a support num")
association_rules = apriori(entries, min_support=0.008, min_confidence=0.7, max_lenght=2)

iterations = 0
correction = {}

for item in association_rules:
    correction.setdefault(item[0][0], {})[item[0][1]]=1

    print(' -> '.join(item[0]))

    print('support: ', str(item[1]))
    print('confidence: ', str(item[2][0][2]))
    print('lift: ' + str(item[2][0][3]))
    print()
    iterations += 1

print("number of rules: ", iterations)
# second fp-growth approach
for itemset in find_frequent_itemsets(entries, 0.02):
    print(itemset)
