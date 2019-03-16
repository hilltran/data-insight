while True:
  user_input = input("Enter a number ")
  user_input == 'done':break
  try:
    number = float(user_input)
    count += 1
  except:
    print('Invalid input')
    continue
  if biggest is None or number > biggest :
    biggest = number
  if smallest is None or number < smallest:
    smallest = number
  # if number > biggest:
  #   biggest = number
  # if number < smallest:
  #   smallest = number
print(f'Biggest Number is {biggest} and the Smallest Number is {smallest}')
##Code Start______
