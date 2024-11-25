# get remaining currency
pesos = float(input('How many Pesos do you have?\n'))
soles = float(input('How many Soles do you have left?\n'))
reais = float(input('How many reais do you have left?\n'))
#convert into dollars usin exchange rates
dollar = str((pesos*0.049) + (soles*0.26) + (reais*0.17))
#print ammount in dollars
print ('You have $' + dollar + 'in currency')
