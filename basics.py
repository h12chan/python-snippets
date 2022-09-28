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

# conditional statement
x = 0
if x==0:
  print(x) # 0
else:
  print(1) # 1
  
# chained conditional
x = 0
if x==1:
  print(x)
elif x==2:
  print(x)
elif x==3:
  print(x)
else:
  print(x)

# for loop
for x in range(1,10):
  print(x) # 1,2,3,4,5,6,7,8,9
  
# for loop complex items
for (x, y) in [("a",1), ("b",2), ("c",3), ("d",4)]:
  print (x,y) # 'a 1' 'b 2' 'c 3' 'c 4'
  
# while loop
x = 1
while x < 5:
  print(x) # 1,2,3,4
  i += 1
  
# nested for loop
for x in range(1,5):
  for y in range(1,x+1):
    print(x, ' ', y) # '1 1' '2 1' '2 2' '3 1' '3 2' '3 3'...
    
# break, continue, pass
for x in range(1,9):
  if x==3:
    continue # skips the rest of the loop
  elif x==4:
    pass # does nothing and continues with rest of the loop
  elif x==5:
    break # stops the loop
    
# Number system prefix for Python numbers
print(bin(5))    #Output: 0b101
print(oct(10))  #Output: 0o12
print(hex(20)) #Output: 0x14

print(0b101)   #Output: 5
print(0o12 + 0o12)  #Output: 20
print(0x14 + 0x14)  #Output: 40

# List Comprehension
squares = [x**2 for x in range(10)]
squares # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
