
from os import listdir
from os.path import isfile, join
from sklearn import preprocessing

from apyori import apriori
import pyfpgrowth
from fp_growth import find_frequent_itemsets

path = './advancedDependencies/'
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
print("unique vals: ", len(set(x for y in entries for x in y)))

