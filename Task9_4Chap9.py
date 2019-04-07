# Exercise 1: Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# ##Code Start______
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     for word in words:
#         # print(word)
#         d[word] = 'defautl_val'
# print(d)
# ## End Code______
#
# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

# ##Code Start______
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# day = []
# count = 0
# for line in fhand:
#     words = line.split()
#     if not words:
#         continue
#     else:
#         if words[0]=='From':
#             day.append(words[2])
#             count = day.count(words[2])
#             d[words[2]] = count
#         else:
#             continue
# print(d)
# print(day)
# ## End Code______

# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
# ##Code Start______
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# emails = []
# count = 0
# for line in fhand:
#     words = line.split()
#     if not words:
#         continue
#     else:
#         if words[0]=='From':
#             emails.append(words[1])
#             count = emails.count(words[1])
#             d[words[1]] = count
#         else:
#             continue
# print(d)
# ## End Code______

# Excercise: 4
#
#
# ##Code Start______
# d={}
# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# emails = []
# count = 0
# counts = 0
# for line in fhand:
#     words = line.split()
#     if not words:
#         continue
#     else:
#         if words[0]=='From':
#             # print(words)
#             emails.append(words[1])
#             count = emails.count(words[1])
#             d[words[1]] = count
#         else:
#             continue
#
# highest_count = max(d, key=d.get)
# print(highest_count, d[highest_count])
# ## End Code______

# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

##Code Start______
d={}
fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
count = 0
domain = []
split = []
for line in fhand:
    words = line.split()
    # print(words)
    if not words:
        continue
    else:
        if words[0]=='From':
            # print(words)
            split = words[1].rsplit('@', 1)
            domain.append(split[1])
            count = domain.count(split[1])
            d[split[1]] = count
        else:
            continue
print(d)
## End Code______
