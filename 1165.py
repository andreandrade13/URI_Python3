n = int(input())

for i in range(0, n):
    num = int(input())
    s = 0
    j = 1
    while(j <= num):
        if(num % j == 0):
            s += 1
        j += 1
    if(s > 2):
        print("%d nao eh primo" %num)
    else:
        print("%d eh primo" %num)
