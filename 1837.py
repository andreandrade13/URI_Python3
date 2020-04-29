a,b=input().split()
a=int(a)
b=int(b)

if(a<0 and b>0):
    q=int(a/b)-1
    r=a-(b*q)
    print(q,end=" ")
    print(r)

elif(a>0 and b<0):
    q=int(a/b)
    r=a-(b*q)
    print(q,end=" ")
    print(r)

elif(a>0 and b>0):
    q=int(a/b)
    r=a-(b*q)
    print(q,end=" ")
    print(r)

elif(a<0 and b<0):
    q=int(a/b)-1
    r=a-(b*q)
    print(q,end=" ")
    print(r) 
    
    
    def euclidean_division(a, b):

    if(a < 0 and b > 0):
        q = int(a/b) - 1
        r = a - (b*q)

    elif(a > 0 and b < 0):
        q = int(a/b)
        r = a - (b*q)

    elif(a > 0 and b > 0):
        q = int(a/b)
        r = a - (b*q)

    elif(a < 0 and b < 0):
        q = int((a+b)/b)
        r = a - (b*q)

    return q, r  

def main():
    print("Please insert two integer values separated by a space")
    print("NOTE: the second integer is NOT allowed to be equal to zero")
    first_input, second_input = input().split()
    first_int=int(first_input)
    second_int=int(second_input)

    if(second_int != 0):
        first_output, second_output = euclidean_division(first_int, second_int)
        print("q = " + str(first_output) + " r = " + str(second_output))
    else:
        print("Second integer must be other than 0")
        print("Try again\n")
        main()

if __name__ == "__main__":
    main()
