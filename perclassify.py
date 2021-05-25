import os
import ast
import random
import sys
import math

inputs = sys.argv
input_path = inputs[1]

#Reading spam and ham model
f = open("percmodel.txt", "r")
model = ast.literal_eval(f.readline())
beta = model['Beta_constant']
print("Beta: ", beta)
# print(type(ham))

#Read input file path
path = [x[0] for x in os.walk(input_path)]
# print('Path: ', path)

#Assign all files to the list
files = []
for i in path:
    _, _, oned_files = next(os.walk(i))
    for j in oned_files: 
        if ('spam' in j ) or ('ham' in j): 
            files.append(i +'/'+j)
print('Length of the files: ', len(files))

#Assign prediction
hams = 0
spams = 0
f = open("percoutput.txt","w")
for file1 in files: 
    words_one_file = []
    # print(file1)
    with open(file1,"r", encoding="latin1") as f1:
        all_data = [line.strip() for line in f1.readlines()]
        # print('All data: ', all_data)
        for j in all_data:
            split = j.split(' ')
            for k in split:
                words_one_file.append(k)
    alpha = 0
    for j in words_one_file:
        if j in model:
            alpha += model[j]
    if alpha > 0:
        spams += 1
        f.write(('Spam' + " " + os.path.abspath(file1)))
        f.write('\n')
    else:
        hams += 1
        f.write('Ham' + " " + os.path.abspath(file1))
        f.write('\n')
f.close()
print("Number of Spam files: ", spams)
print("Number of NOT Spam files: ", hams)