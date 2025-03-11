# Factorial of give number
# Method 1
# num=int(input("Enter a number:"))
# fact=1
# if num==0:
#     print("The factorial of 0 is ",1)
# if num<0:
#     print("Factorial does not exist")
# if num>0:
#     for i in range(1,num+1):
#         fact=fact*i
#     print("The factorial of given number is",fact)

# Method 2
def fact(num):
    if(num==0):
        return 1
    elif(num<0):
        return  "not exist"
    else:
        return num*fact(num-1)
   
        
num=int(input("Enter the number:"))
result=fact(num)
print("The factorial of number is",result)






