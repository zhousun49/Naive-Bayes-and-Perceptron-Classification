import os
import ast
import random
import sys
import math

inputs = sys.argv
input_path = inputs[1]

#Reading spam and ham model
f = open("nbmodel.txt", "r")
spam = ast.literal_eval(f.readline())
ham = ast.literal_eval(f.readline())
P_spam = spam['P_spam']
P_ham = ham['P_ham']
print("Probability of Spam: ", P_spam)
print("Probability of Ham: ", P_ham)
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
f = open("nboutput.txt","w")
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
    P_message_spam = 0
    P_message_ham = 0
    # print("Length of the file: ", len(words_one_file))
    for word in words_one_file:
        #Skip words not in the dictionary
        if word in spam: 
            # print(spam[word])
            # print(ham[word])
            P_message_spam += math.log(spam[word])
            # print(P_message_spam)
            P_message_ham += math.log(ham[word])
        
    # print('spam message: ', P_message_spam)
    # print('ham message: ', P_message_ham)
    P_spam_message = math.log(P_spam) + P_message_spam
    P_ham_message = math.log(P_ham)  + P_message_ham
    # print('Probably of spam message: ', P_spam_message)
    # print('Probably of ham message: ', P_ham_message)
    if P_ham_message > P_spam_message:
        hams += 1
        f.write(('Ham' + " " + os.path.abspath(file1)))
        f.write('\n')
    elif P_ham_message < P_spam_message:
        spams += 1
        f.write('Spam' + " " + os.path.abspath(file1))
        f.write('\n')
f.close()
print("Number of Spam files: ", spams)
print("Number of NOT Spam files: ", hams)