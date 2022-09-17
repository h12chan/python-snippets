people = ['John','Mary','Ben','Paul']
John = ['carpenter','30']
Mary = ['teacher','32']
people = [John, Mary]
print(people)
numbers = [1,2,3,4,5,6,7]
print(numbers)
numbers = [0, None] # empty equivalents
numbers = [3] * 5
print(numbers)
numbers = [1,2,3,4,5]
print(numbers[0:2]) # slice
print(numbers[-1]) # negative begins from end at -1
numbers = [1,2,5,6,7,8]
numbers[2:-4] = [3,4] # slice insert
print(numbers)
print(len(numbers)) # length of list
print(max(numbers)) # get max in array
print(min(numbers)) # get min in array
print(3 in numbers) # get 3 in array
print('teacher' in people[1]) # get carpenter in people
name = 'John'
john = list(name)
print(john)
john[4:] = list('son')
print(john)
