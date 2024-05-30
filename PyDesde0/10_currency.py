#leftover cash
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

#///////////////////////operations/////////////////////////

#pesos
leftpesos = pesos * 0.00026

#soles
leftsoles = soles * 0.27

#reais
leftreais = reais * 0.19

total = leftpesos + leftsoles + leftreais
print(total)