al = 0
ga = 0
di = 0
x = 0

while(x != 4):
    x = int(input())
    if(x == 1):
        al += 1
    elif(x == 2):
        ga += 1
    elif(x == 3):
        di += 1
        
print('MUITO OBRIGADO')
print('Alcool: %d' %al)
print('Gasolina: %d' %ga)
print('Diesel: %d' %di)
    
