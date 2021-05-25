import os
import random
import numpy as np
import sys
import random

inputs = sys.argv
input_path = inputs[1]

#Reading necessary files
path = [x[0] for x in os.walk(input_path)]
# print('Path: ', path)

files = []
for i in path:
    # print('Directory: ', i)
    dirt = i
    _, _, oned_files = next(os.walk(dirt))
    # print(i, " has ", len(oned_spam_files), ' files')
    for j in oned_files:
        if ('spam' in i ) or ('ham' in i): 
            files.append(dirt+'/'+j)

#Get words from files
words = []
for f in files: 
    with open(f,"r", encoding="latin1") as f1:
        all_data = [line.strip() for line in f1.readlines()]
        for j in all_data:
            split = j.split(' ')
            for k in split:
                words.append(k)
# print(words)

#Count unique words and create a dictionary for unique words
unique_words = np.unique(words)
print("Length of unique words: ", len(unique_words))
zeros = [0]*len(unique_words)

#Initialize contants 
wd = dict(zip(unique_words, zeros)) 
wd['\x00'] = 0
b = 0
ud = dict(zip(unique_words, zeros))
ud['\x00'] = 0
beta = 0
c = 0

#Should be start of the iteration loop, here use Max interation = 1 
###
for iteration in range(100): 
    print('Iteration number: ', iteration+ 1)
    random.shuffle(files)
    # print(files)
    # ten_files = random.sample(files, 1000)
    for f in files: 
        #Assign value of y
        if ('spam' in f):
            y = 1
        elif ('ham' in f):
            y = -1
        #Append words of a single file to a list
        word_one_file = []
        with open(f,"r", encoding="latin1") as f1:
            all_data = [line.strip() for line in f1.readlines()]
            for j in all_data:
                split = j.split(' ')
                for k in split:
                    word_one_file.append(k)
        #Calculation of alpha
        alpha = 0
        for word in word_one_file:
            # print("word: ", word)
            # if word == '\x00':
            #     print('hahahahah')
            #     continue
            alpha += wd[word]
        alpha += b
        #In case weight change is needed
        if y * alpha <= 0: 
            b += y
            # print('b: ', b)
            beta += y*c
            # print(word_one_file)
            for w in word_one_file:
                # print(w)
                wd[w] += y
                ud[w] += y*c
                # print(ud[w])
        c += 1
beta = b - 1/c*beta
for i in ud:
    ud[i] = wd[i] - 1/c*ud[i]
ud['Beta_constant'] = beta

f = open("percmodel.txt","w")
f.write(str(ud))
f.close()