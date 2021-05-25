import os
import random
import numpy as np
import sys

inputs = sys.argv
input_path = inputs[1]

#Reading necessary files
path = [x[0] for x in os.walk(input_path)]
# print('Path: ', path)

spam_files = []
ham_files = []
for i in path:
    # print('Directory: ', i)
    if 'spam' in i:
        spam_dir = i
        _, _, oned_spam_files = next(os.walk(spam_dir))
        # print(i, " has ", len(oned_spam_files), ' files')
        for j in oned_spam_files:
            spam_files.append(spam_dir+'/'+j)
    elif 'ham' in i: 
        ham_dir = i 
        _, _, oned_ham_files = next(os.walk(ham_dir))
        # print(i, " has ", len(oned_ham_files), ' files')
        for j in oned_ham_files:
            ham_files.append(ham_dir+'/'+j)

#Calculate P_spam and P_ham
print('Total spam files: ', len(spam_files))
print('Total ham files: ', len(ham_files))
P_spam = len(spam_files)/(len(spam_files)+len(ham_files))
P_ham = len(ham_files)/(len(spam_files)+len(ham_files))
print('Probability of Spam: ', P_spam)
print('Probability of Ham: ', P_ham)

#Get words from files
spam_words = []
for spam in spam_files: 
    with open(spam,"r", encoding="latin1") as f1:
        all_data = [line.strip() for line in f1.readlines()]
        for j in all_data:
            split = j.split(' ')
            for k in split:
                spam_words.append(k)
print("Length of Spam words: ", len(spam_words))
ham_words = []
for ham in ham_files: 
    with open(ham,"r", encoding="latin1") as f1:
        all_data = [line.strip() for line in f1.readlines()]
        for j in all_data:
            split = j.split(' ')
            for k in split:
                ham_words.append(k) 
print("Length of Ham words: ", len(ham_words))

#Assign a dictionary for saving
spam_dic = {}
ham_dic = {}
spam_dic['P_spam'] = P_spam
ham_dic['P_ham'] = P_ham

#Count unique words
unique_spam, counts1 = np.unique(spam_words, return_counts=True)
spam_wordcount = dict(zip(unique_spam, counts1))
# for j in spam_wordcount:
#     print(spam_wordcount[j])
unique_ham, counts2 = np.unique(ham_words, return_counts=True)
ham_wordcount = dict(zip(unique_ham, counts2))
words = np.append(unique_spam, unique_ham)
unique_words = np.unique(words)
print("Length of unique spam words: ", len(unique_spam))
print("Length of unique ham words: ", len(unique_ham))
print("Length of unique words: ", len(unique_words))
total_word_spam = len(spam_words)+ len(unique_words)
total_word_ham = len(ham_words)+ len(unique_words)
print("Total word spam: ", total_word_spam)
print("Total word ham: ", total_word_ham)

#Assign a loop to calculate probability
i = 0
for j in unique_words:
    i += 1
    if i%10000 == 0: 
        print("No. ", i, " element added")
    # spam_dic[j] = (spam_wordcount[j] + 1)/total_word_spam
    # ham_dic[j] = (ham_wordcount[j]  + 1)/total_word_ham
    if j in unique_spam: 
        spam_dic[j] = (spam_wordcount[j] + 1)/total_word_spam
    else:
        spam_dic[j] = 1/total_word_spam

i = 0
for j in unique_words:
    i += 1
    if i%10000 == 0: 
        print("No. ", i, " element added")
    if j in unique_ham: 
        ham_dic[j] = (ham_wordcount[j]  + 1)/total_word_ham
    else:
        ham_dic[j] = 1/total_word_ham

print('Length of dictionary: ', len(ham_dic))

#Save to file
f = open("nbmodel.txt","w")
f.write(str(spam_dic))
f = open("nbmodel.txt","a")
f.write('\n')
f.write(str(ham_dic))
f.close()
