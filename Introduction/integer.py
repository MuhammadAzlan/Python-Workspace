# + - % / *
# claculate
x = input("Enter first number: ")
y= input("Enter second number: ")
print(x + y)# prints 24 (because it concatenates the string)

p=int(x) + int(y)
print(p)

# other way
q= int(input("Enter first number: "))
z= int(input("Enter second number: "))
print(q*z)

t= int(input("Enter first number: ")) - int(input("Enter second number: "))
print(t)

#  FLOAT
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c= a/b
print(c)

# round() of the number
d= round(c)
print(d)
print(round(c, 2))

# other way
print(f"{d:,}")
print(f"{c:,.2f}")
