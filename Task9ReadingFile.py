d = {}
fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        d[word]= 'default'
print(d)
