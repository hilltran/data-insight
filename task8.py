count = 0
fhand = open('//Users//nightowl//Desktop//5WeeksPythonDevCourse//mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2: continue
    if words[0] != "From": continue
    count += 1
    print(words[1])

    # else:
    #     continue
print(f'There were {words} lines in the file with From as the first word')
