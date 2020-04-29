V = int(input())
N = [1,2,4,8,16,32,64, 128, 256, 512]

for i in range(len(N)):
  N[i] = N[i]*V 
  
      
  
  
  
for i in range(len(N)):
 print("N[" + str(i) + "] = " + str(N[i]))
