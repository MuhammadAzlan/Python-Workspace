#Creating a function using keyword def
def hello():
    print("Hello", sep=" ")
name=input("What's your name? ")
hello()
print(name)


#to understand
print("what your favourite number?")
number= input()
print(f"Your favourite number is: {number}")

def hello(to):
    print(f"Hello, {to}!")
name=input("What's your name? ")
hello(name)    

# define default value in arguments
def hello(to="world"):
    print(f"Hello, {to}!")
hello()    
name=input("What's your name? ")
hello(name)

#using main() function to call the hello() function
def main():
    name=input("what's your name? ")
    hello(name)

def hello(to):
    print(f"Hello, {to}!")    
    
main()    

# return variables
def main():
    x= int(input("what's your x ? "))
    print("the square of x is:", square(x))
    
def square(n):  
    return n*n #pow(n,2). n ** 2

main()