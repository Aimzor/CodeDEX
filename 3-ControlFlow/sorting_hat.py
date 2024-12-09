# 
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print(' /|      Welcome to Hogwarts School of Witchcraft and Wizardry      |\\')
print(' \|               Place the sorting hat on your head                |/')
print(' /|                You’ll be sorted into your house                 |\\')
print(' \|              Don’t fear, embrace the hat’s wisdom!              |/\n')

print('Q1) Do you like Dawn or Dusk?\n      1) Dawn\n      2) Dusk\n')
answer = int(input('What is your answer, 1 or 2?\n'))

if answer == 1:
  gryffindor = +1 
  ravenclaw = +1
elif answer == 2: 
  hufflepuff = +1
  slytherin = +1
else:
  print('Wrong input')
print(gryffindor)

print('Q2) When I’m dead, I want people to remember me as:\n      1) The Good\n      2) The Great\n      3) The Wise\n      4) The Bold\n')
answer = int(input('What is your answer, 1-4?\n'))

if answer == 1:
  hufflepuff = +2
elif answer == 2:
  slytherin = +2
elif answer == 3: 
  ravenclaw = +2
elif answer == 4:
  gryffindor = +2
else:
  print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?\n      1) The violin\n      2) The trumpet\n      3) The piano\n      4) The drum\n')
answer = int(input('What is your answer, 1-4?\n'))

if answer == 1:
  slytherin = +4
elif answer == 2:
  hufflepuff = +4
elif answer == 3: 
  ravenclaw = +4
elif answer == 4:
  gryffindor = +4
else:
  print('Wrong input')

print('\nGryffindor: ', gryffindor)
print('Ravenclaw: ', ravenclaw) 
print('Hufflepuff: ', hufflepuff)
print('Slytherin: ', slytherin)

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print('\nhmmm yes, you belong in...GRYTHINDOR!!')
elif ravenclaw > hufflepuff and  ravenclaw > slytherin:
  print('\nhmmm yes, you belong in...RAVENCLAW!!')
elif  hufflepuff > slytherin:
  print('\nhmmm yes, you belong in...HUFFLEPUFF!!')
elif slytherin:
   print('\nhmmm yes, you belong in...SLYTHERIN!!')
else:
  print('\nI\'m afraid...you are a muggle. You will now be obliterated')