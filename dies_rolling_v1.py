import random

while True:
  option =input('Do you want to roll the dice? (y/n) : ').lower()
  if option == 'y':
      dice1 = random.randint(1 , 6)
      dice2 = random.randint(1 , 6)
      print(f'dice1 : {dice1} and dice2 : {dice2}')
  elif option == 'n':
      print('Thank you! Visit again.')
      break
  else:
      print('Invalid choice ! please enter rightn choice (y/n)')
