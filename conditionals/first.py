# # > >= < <= == !=
# # if statement
# def main():
#     a =int(input("Enter a number x: "))
#     b = int(input("Enter a number y: "))
#     ans(a,b)

# def ans(x,y):

#     if x>y:
#         print(f"{x} is greater than {y}")
#     if x<y:
#         print(f"{x} is less than {y}")
#     if x==y:
#         print(f"{x} is equal to {y}")        
    
# for i in range(0,3):          
#     main()  
 
#  #elif statement     
# x =int(input("Enter a number x: "))
# y = int(input("Enter a number y: "))      

# if x>y:
#     print(f"{x} is greater than {y}")
# elif x<y:
#     print(f"{x} is less than {y}")
# elif x==y:
#     print(f"{x} is equal to {y}")  
    
 
#else statement  
x =int(input("Enter a number x: "))
y = int(input("Enter a number y: "))      

if x>y:
    print(f"{x} is greater than {y}")
elif x<y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")     
    
#or and operator
if x>y or x<y: # x != y
    print(f"{x} is not equal to {y}")

else:
    print(f"{x} is equal to {y}")       