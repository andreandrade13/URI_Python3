import math

n = int(input())

if n >= 17 and n <= 1000000000:
    minimo = n / math.log(n)
    maximo = 1.25506 * minimo
    
print('%.1f %.1f' %(minimo,maximo))
