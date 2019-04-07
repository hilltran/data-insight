##Start Excercise_________________________________________
# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

##Code Start______
#1. a function "chop" return None
# def chop(var):
#   tail = var[1:]
#   head = tail[:1]
#   return None
# print(chop(x))

# 1. b
# def middle(cut):
#   tail = cut[1:]
#   head = tail[:-1]
#   return head

# print(middle(x))
## End Code______
# fname = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt', 'r')
# # fname = input('Enter the file name: ')
# fhand = fname.read()
# count = 0
# # for line in fhand:
# #     print(line.upper())
# print(fhand.upper())

##Start Excercise_________________________________________
# Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

##Code Start______

fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
for line in fhand:
    words = line.split()
    # print('Debug', words)
    if len(words) == 0: continue
    if words[0] != 'From' : continue
    print(words[2])

# Above code fail if it ran uses the same code for file 'mbox-short2.txt'

# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short2.txt')
# for line in fhand:
#     words = line.split()
#     # print('Debug', words)
#     if len(words) <= 1: continue #safe guard here to ensure if it one word/letter it will not print
#     if words[0] != 'From' :
#         continue
#     print(words[2])

## End Code______

# Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the and logical operator with a single if statement.

##Code Start______
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short2.txt') #mbox-short2.txt has several lines with only "From"
# for line in fhand:
#     words = line.split()
#     # print('Debug', words)
#     if len(words) <= 1 or words[0] != 'From':
#         continue
#     print(words[2])
## End Code______

#Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
from typing import List, Any

# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//romeo.txt')
# romeo_list = []
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word in romeo_list: continue
#         romeo_list.append(word)
#
#         # if words not in romeo_list:
# romeo_list.sort()
# print(romeo_list)

# Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.
# count = 0
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     if len(words) <= 1 or words[0] != 'From':
#         continue
#     if words[0] == "From":
#         print(words[1])
#         count += 1
# print(f'There were {count} lines in the file with From as the first word')

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done". Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

# num_list = []
# while True:
#     num_enter = input('Enter a number ')
#     if num_enter == 'done': break
#     try:
#         number= float(num_enter)
#         num_list.append(number)
#     except:
#         print('Invalid input')
#
# print(f'Maximum: {max(num_list)} \nMinimum: {min(num_list)}')

##Code Start______
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//words.txt')
# d = dict()
# for line in fhand:
#     words = line.split()
#     if words not in d:
#         d[words] = 1
#     else:
#         d[words] += 1
# print(d)
## End Code______
#
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//words.txt')
# d = dict()
# for line in fhand:
#     words = line.split()
#     print(words)
#     if words[0] not in d:
#         d[words[0]] = 1
#     else:
#         d[words[0]] += 1
# print(d)


# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)
#
# d = {}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//words.txt')
# for line in fhand:
#     words = line.split()
#     for word in words:
#         d(word)= 'default'
# print(d)
#



# d = {}
# fhand = requests.get('https://www.py4e.com/code3/words.txt')
# for line in fhand:
#   words = line.split()
#   # print(words)
#   for word in words:
#     d[word] = 'default'
#     #  d['word'] = 'default'
#   # print('Debug', words)
# print(d)

# Updating existing key's value
# wordFreqDic.update(Hello = 99 )
