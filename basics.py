# comment declaration

# code blocks determined by indentation

# variable declaration
mark = 90
print(mark)

# basic data types
a = "abc"
print(a, "is of type", type(a))
a = 6
print(a, "is an integer?", isinstance(a,int))

# pass by reference
num1 = 90
num2 = num1
print(id(num1), id(num2))

# input
number = input('What is your mark? ')
print(number)

# typecasting
number1, number2 = input('What is your first mark? '), input('What is your second mark?')
number1 = int(number1)
number2 = int(number2)
sum = number1 + number2
print(sum)

# print f example 1
number1, number2 = input('What is your first mark? '), input('What is your second mark?')
number1 = int(number1)
number2 = int(number2)
print(f'The first number is {number1}, and the second number is {number2}.')

# print f example 2
name, profession = "Joe Schmol", "carpenter"
height, age = 180, 30
print(f'{name} was a professional {profession} at age {age} and height {height}')

# BODMAS
print(6-2+3)

# AND, OR
# and has precedence over or
True and False or True # True
