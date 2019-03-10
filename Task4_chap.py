
# ##Start Excercise_________________________________________
# Exercise 1: Ran code in terminal
# import random

#  random.randint(5, 10)
# 10
#  random.randint(5, 10)
# 9
#  t =[21,22,32]
#  random.choice(t)
# 21
#  t=[1,3,6]
#  random.choice(t)
# 1
#  t=[32,20,33]
#  random.choice(t)
# 33

# ##Start Excercise_________________________________________
# Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
# repeat_lyrics()
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# Answer: the following errors_______________________
# Traceback (most recent call last):
#   File "main.py", line 16, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

# ##Start Excercise_________________________________________
# Exercise 3:

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# repeat_lyrics()

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# Answer: the following errors_______________________
# Traceback (most recent call last):
#   File "main.py", line 18, in <module>
#     ___________
# NameError: name '___________' is not defined

# ##Start Excercise_________________________________________
# Exercise 4: What is the purpose of the "def" keyword in Python?
# Answer is d) both true -It indicates the start of a function & It indicates that the following indented section of code is to be stored for later

# ##Start Excercise_________________________________________
# Exercise 5:
# Answer is d)

# ##Start Excercise_________________________________________
# Exercise 6:
##Code Start-my version 1______
# def computepay(hours,rate):
#   if hours > 0 and rate > 0:
#     if hours > 40:
#       pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
#     else:
#       pay = (hours * rate)
#     return pay
#   else:
#     print('please check hours or rates')
## End Code______

##Code Start- my version 1.4______
# def computepay(hours,rate):
#   try:
#     hours = float(hours)
#     rate = float(rate)
#     if hours > 0 and rate > 0:
#       if hours >= 40:
#         pay = (40 * rate) + ((hours - 40) *1.5*rate)
#         return pay
#       else:
#         pay = (hours * rate)
#         return pay
#   except:
#     print('please check hours or rates')

# print(computepay(41,10))
# print(computepay(41,0))
# print(computepay(41,1))
# print(computepay(41,"hello"))
## End Code______

# ##Start Excercise_________________________________________
# Exercise 7:
##Code Start______

def computegrade(score):
  try:
    score = float(score)
    if score >= 0.9 and score <=1.0:
      return "A"
    elif score >= 0.8 and score <0.9:
      return "B"
    elif score >= 0.7 and score <0.8:
      return "C"
    elif score >= 0.6 and score <0.7:
      return "D"
    elif score < 0.5 and score >=0 :
      return "F"
    else:
      return "Bad Score"
  except:
    return "Bad Score"

prompt = "Please enter score between 0.0 and 1.0\n"
enter_score = (input(prompt))
print(computegrade(enter_score))
## End Code______

# ##Code Start______Version 2 on 10-3-19
# score = None
# prompt = "Please enter score between 0.0 and 1.0\n"
# score = (input(prompt))
# while score != None:
#   try:
#     if score > 0 and score < 1:
#       score = float(score)
#   except:
#     print("Please enter score between 0.0 and 1.0")
#     break
# score = (input("Enter only score between 0.0 and 1.0 \n"))
# # try:
# # score > 0 and score < 1:
# score = float(score)
# # except:
# #   print("Please enter score between 0.0 and 1.0 next time. Goodbye")
# #   quit()
# if score >= 0.9 and score <=1.0:
#   print("A")
# elif score >= 0.8:
#   print("B")
# elif score >= 0.7:
#   print("C")
# elif score >= 0.6:
#   print("D")
# elif score < 0.5:
#   print("F")
# else:
#   print("Bad Score")
# ## End Code______

# ##Code Start______Version 3 on 10-3-19
score = None
prompt = "Please enter score between 0.0 and 1.0\n"
score = (input(prompt))
while score != None:
  try:
    if score > 0 and score < 1:
      score = float(score)
  except:
    break
score = (input("Enter only score between 0.0 and 1.0 \n"))
try:
  score = float(score)
except:
  print("Please enter score between 0.0 and 1.0 next time. Goodbye")
  quit()
if score >= 0.9 and score <=1.0:
  print("A")
elif score >= 0.8 and score <0.9:
  print("B")
elif score >= 0.7 and score <0.8:
  print("C")
elif score >= 0.6 and score <0.7:
  print("D")
elif score < 0.5 and score >=0: # the reason for not using 'elif score >= 0.8' instead of 'elif score >= 0.8 and score <0.9:' because if it a number larger or = to 1 or 0 or -minus number it would get a grade.
  print("F")
else:
  print("Bad Score")

# ## End Code______
