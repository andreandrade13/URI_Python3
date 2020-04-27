a = int(input())
b = int(input())

t = a

if(a > b):
    a = b
    b = t
    
while(a < b):
    a += 1
    if(a % 5 == 2 or a % 5 == 3 and a != b):
        print(a)
