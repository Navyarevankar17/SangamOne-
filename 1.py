n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if(n1>n2):
    if(n2>n3):
        print(n1)
    else:
        print(n2)
elif(n1>n3):
    print(n1)
else:
    print(n3)
    
