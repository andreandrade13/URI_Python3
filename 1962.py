entrada = int(input())

while entrada > 0:
    ano = int(input())
    if ano <= 2014:
        print('%d D.C.' %(2015 - ano))
    else:
        print('%d A.C.' %(ano - 2015))
    entrada -= 1
