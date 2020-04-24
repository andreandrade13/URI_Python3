imp1 = int(input())
imp2 = int(input())

soma = 0

if(imp1 > imp2):
    t = imp1
    imp1 = imp2
    imp2 = t
    
if(imp1 % 2 != 0):
    imp1 += 2
    while(imp1 < imp2):
        if(imp1 % 2 != 0):
            soma += imp1
        imp1 += 1
        
else:
    imp1 += 1
    while(imp1 < imp2):
        if(imp1 % 2 != 0):
            soma += imp1
        imp1 += 1
        
print(soma)
