# comment declaration

# code blocks determined by indentation

# variable declaration
mark = 90
print(mark)

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

# print f
number1, number2 = input('What is your first mark? '), input('What is your second mark?')
number1 = int(number1)
number2 = int(number2)
print(f'The first number is {number1}, and the second number is {number2}.')

# BODMAS
print(6-2+3)

# AND, OR
TRUE AND FALSE OR TRUE # TRUE
