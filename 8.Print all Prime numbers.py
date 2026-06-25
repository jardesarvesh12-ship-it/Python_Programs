num = int(input("enter number :"))

x=0

for i in range(1,num+1):
    if(num%i==0):
        x= x + 1

if(x == 2):
    print("prime number: ")
else:
    print("even number: ")




  

5