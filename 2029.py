while True:
    try:
        v = float(input())
        d = float(input())
        
        r = d/2
        a = 3.14*r*r
        h = v/a
        
        print('ALTURA = %.2F' %h)
        print('AREA = %.2f' %a)
    except:
        break
