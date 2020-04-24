qtd = int(input())

s = 0
n = 0

for i in range(qtd):
    valor = int(input())
    if(valor >= 10 and valor <= 20):
        s += 1
    else:
        n += 1

print("%d in" %s)
print("%d out" %n)
