import sys

inputs = sys.argv
output = inputs[1]
# print(output)

#Calculate metrics needed for Precision, recall and F1
true_positive_ham = 0
false_positive_ham = 0
false_negative_ham = 0
true_positive_spam = 0
false_positive_spam = 0
false_negative_spam = 0
with open(output,"r", encoding="latin1") as f1:
    all_data = [line.strip() for line in f1.readlines()]
    for i in all_data:
        single_line = i.split(" ")
        classfication = single_line[0].lower()
        # print('ham' in single_line[1])
        # print(single_line[-1])
        if (classfication == "ham") and ("ham" in single_line[-1]):
            true_positive_ham += 1
        elif (classfication == "ham") and ("spam" in single_line[-1]):
            false_positive_ham += 1
            false_negative_spam += 1
        elif (classfication == "spam") and ("spam" in single_line[-1]):
            true_positive_spam += 1
        elif (classfication == "spam") and ("ham" in single_line[-1]):
            false_positive_spam += 1 
            false_negative_ham += 1
# print(true_positive_spam)

precision_ham = true_positive_ham/(true_positive_ham + false_positive_ham)
recall_ham = true_positive_ham/(true_positive_ham + false_negative_ham)
f1_ham = 2*precision_ham*recall_ham/(precision_ham + recall_ham)
precision_spam = true_positive_spam/(true_positive_spam + false_positive_spam)
recall_spam = true_positive_spam/(true_positive_spam + false_negative_spam)
f1_spam = 2*precision_spam*recall_spam/(precision_spam + recall_spam)

print('Precision of Ham: ', precision_ham)
print('Recall of Ham: ', recall_ham)
print('F1 Score of Ham: ', f1_ham)
print('Precision of Spam: ', precision_spam)
print('Recall of Spam: ', recall_spam)
print('F1 Score of Spam: ', f1_spam)
