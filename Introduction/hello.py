#str
print("hello,world")

#ask from user input
name = input("What is your name? ")

#Print the output/ Say hello to user
print("Hello, " + name + "!")
print("Hello, {}!".format(name))
print(f"Hello, {name}!")

# next line
print("hello,world\n")
print("hello,world", end=" ")
#separate spaces
print("hello,world", sep=" ")

# Remove whitespace from string
str1 = "   hello,world   "
str1 =str1.strip()
print(str1)

#Capitalize the first letter of the string
name = name.capitalize()
print(name)
#title case
name = name.title()
print(name)

#other ways
book = input("What is your favorite book? ").capitalize().title()
print(f"Your favorite book is: {book}")

#split String
book1 = book.split(" ")
print(f"Hello, {book1}")
first, last = book.split(" ")
print(f"First name: {first}")