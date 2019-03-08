# Exercise 1: Type the following statements in the Python interpreter to see what they do:
5
x = 5
x + 1

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
name = input('Enter your name: ')
print('Hello ' + name)
f
# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) + float(rate)
print('Pay: ' + str(pay))

# Exercise 4: Assume that we execute the following assignment statements:
# width = 17 height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 1.width//2 = 8 Floor division
# 2.width/2.0 = 8.5 Divide resulting in a float
# 3.h3= height/3 Divide resulting in a float
# 4. 1 + 2 * 5 = 11 Operators multiply first and then add

# Exercise 5
# 1.
raw_input = input('Celsius temperature: ')
fahrenheit = (float(raw_input) * 9/5) + 32
print('The temperature in Fahrenheit is '+ str(fahrenheit))

# 2. choose variable name that are mnemonic, means "memory aid".
