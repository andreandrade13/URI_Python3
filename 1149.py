num = input()
lista = num.split()
temp = []
soma = []

cont = 0

for elemento in lista:
  if elemento>"0":
    temp.append(elemento)
    if len(temp)==2:
      break
    
x = int(temp[0])
y = int(temp[1])

while cont<y:
  soma.append(x)
  x = x+1
  cont+=1
  
print(sum(soma))
