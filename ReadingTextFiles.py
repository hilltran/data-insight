
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

# fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     # print('Debug', words)
#     if len(words) == 0: continue
#     if words[0] != 'From' : continue
#     print(words[2])

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
