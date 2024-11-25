# get pH reading
ph = int(input('What is the pH reading (0-14)? : '))
# determine potential of hydrogen
if ph > 7:
  print('Basic')
elif ph < 7:
  print ('Acidic')
else:
  print('Neutral')