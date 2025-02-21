lower=int(input("Enter the lower level value:"))
upper=int(input("Enter the upper level value:"))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                print(num,"not a prime Number")
                break
        else:
                print(num,"prime Number")

       

