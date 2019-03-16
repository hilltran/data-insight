fname = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt', 'r')
# fname = input('Enter the file name: ')
fhand = fname.read()
count = 0
# for line in fhand:
#     print(line.upper())
print(fhand.upper())
