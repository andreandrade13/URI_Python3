x = input()
x = x.split(' ')
n = int(x[0])

for i in range(int(x[0])):
    a = input()
    
if a == 'fechou':
    n += 1
elif a == 'clicou':
    n -= 1

print(n)
