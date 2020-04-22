salario = float(input())

if(salario <= 400.00):
    print("Novo salario: %.2f" %(salario*1.15))
    print("Reajuste ganho: %.2f" %(salario*0.15))
    print("Em percentual: 15 %")

if(400.01 <= salario <= 800.00):
    print("Novo salario: %.2f" %(salario*1.12))
    print("Reajuste ganho: %.2f" %(salario*0.12))
    print("Em percentual: 12 %")

if(800.01 <= salario <= 1200.00):
    print("Novo salario: %.2f" %(salario*1.10))
    print("Reajuste ganho: %.2f" %(salario*0.10))
    print("Em percentual: 10 %")

if(1200.01 <= salario <= 2000.00):
    print("Novo salario: %.2f" %(salario*1.07))
    print("Reajuste ganho: %.2f" %(salario*0.07))
    print("Em percentual: 7 %")

if(salario > 2000.00):
    print("Novo salario: %.2f" %(salario*1.04))
    print("Reajuste ganho: %.2f" %(salario*0.04))
    print("Em percentual: 4 %")   
