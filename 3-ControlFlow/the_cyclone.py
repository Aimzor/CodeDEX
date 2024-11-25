#get riders height and number of credits
height = int(input('How tall are you(cm)? '))
credits = int(input('How many credits do you have? '))
#determine eligibility
if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits <10:
  print('You don\'t have enough credits.')
else: 
  print('You don\'t meet the requiremnts to ride.')