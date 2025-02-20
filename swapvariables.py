# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# c=a
# a=b
# b=c
# print("After swapping")
# print("value of a is :",a)
# print("value of b is :",b)

# Another Method withot including third variable
A=int(input("Enter the value of a:"))
B=int(input("Enter the value of b:"))
A,B=B,A
print("After swapping")
print("value of A is :",A)
print("value of B is :",B)
