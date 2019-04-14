# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

##Code Start______
#
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox.txt')
# day = []
# count = 0
# l = list()
# domain = []
# for line in fhand:
#     words = line.split()
#     if not words:
#         continue
#     else:
#         if words[0]=='From':
#             # print(words)
#             split = words[1].rsplit('@', 1)
#             domain.append(split[1])
#             count = domain.count(split[1])
#             d[split[1]] = count
#         else:
#             continue
#
# key_value = sorted([(v,k) for k,v in d.items() ], reverse=True)
#
# highest_value = [key_value[0:1],key_value[0:0]]
#
# for k, v in highest_value[0]:
#     print(v, k)

# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.


# import string
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//romeo.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
#
# # Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))
#
# lst.sort()
#
# for key, val in lst[:10]:
#     print(key, val)
# ## End Code______


# import string
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
#
# # Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))
#
# lst.sort()
#
# for key, val in lst[:10]:
#     print(key, val)
## End Code______
import string


#####Code Start______
# ## End Code______
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# day = []
# count = 0
# l = list()
# time = []
# for line in fhand:
#     words = line.split()
#     if not words:
#         continue
#     else:
#         if words[0]=='From':
#             # print(words[5])
#             split = words[5].rsplit(':', 2)
#             # print(split[0])
#             time.append(split[0])
#             count = time.count(split[0])
#             d[split[0]] = count
#         else:
#             continue
#
# # # Sort the dictionary by key
# dl = list()
# for key, val in list(d.items()):
#     dl.append((key, val))
#
# dl.sort()
# for p in dl:
#     print(p)
# ## End Code______
#
#
# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

# ##Code Start______
# d = {}
# count = 0
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox.txt')
# # l = list()
# time = []
# for line in fhand:
#     words = line.split()
#     for letters in words:
#         letter = list(letters)
#         for i in letter:
#             if i in alphabet:
#                 if i not in d:
#                     d[i] = 1
#                 else:
#                     d[i] += 1
#
# from operator import itemgetter
# for key, value in sorted(d.items(), key = itemgetter(1)):
#     print(key, value) #lowest to highest.
# ## End Code______
# ____________________

 # for key, value in sorted(d.items(), key = itemgetter(1), reverse = True):
 #    print(key, value)  for reverse order of highest to lowest

# t.sort() did not work with the below even with code only the above
# {k: t[k] for k in sorted(t, key=t.get, reverse=True)}


# # Sort the dictionary by key
# dl = list()
# for key, val in list(d.items()):
#     dl.append((key, val))
#
# dl.sort()
# for p in dl:
#     print(p)
## End Code______

    # print(letters)
    # print(words)

    # for letters in words:
    #     letter = list(s)
    #     print(letter)
    #     if not alphabet:
    #         continue
    #     elif letters in d:
    #         d[letters] = 1
    #     else:
    #         d[letters] = count + 1

# print(d)

# if in list(string.ascii_lowercase):

