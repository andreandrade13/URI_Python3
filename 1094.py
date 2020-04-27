n = int(input())
cont,rato, sapo,coelho = 0,0,0,0

for i in range(n):
    quantia, tipo = input().split()
    str(tipo)
    cont += int(quantia)
    if tipo == 'C':
        coelho += int(quantia)
    elif tipo == 'R':
        rato += int(quantia)
    elif tipo == 'S':
        sapo += int(quantia)
        
print('Total: %d cobaias' %cont)
print('Total de coelhos: %d' %coelho)
print('Total de ratos: %d' %rato)
print('Total de sapos: %d' %sapo)
print('Percentual de coelhos: %.2f' %float(((100 * coelho) / cont)), '%')
print('Percentual de ratos: %.2f' %float(((100 * rato) / cont)), '%')
print('Percentual de sapos: %.2f' %float(((100 * sapo) / cont)), '%')
