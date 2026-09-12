
fruits = ['banana', 'orange', 'mango', 'lemon']
print (len(fruits))
print (fruits[0])
print (fruits[1])
print (fruits[2])
print (fruits[3])
print (fruits[-2])

print ('Fruits List:', fruits)
does_exist = 'banana' in fruits

print ('Does banana exist in the list?')
if does_exist:
    print ('Yes, banana exists in the list')
else:
    print ('No, banana does not exist in the list')

# checking items
does_exist = 'apple' in fruits
print ('Does apple exist in the list?')
if does_exist:
    print ('Yes, apple exists in the list')
else:
    print ('No, apple does not exist in the list')

 # Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
fruits.append('lime')
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
fruits.insert(3, 'lime')
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']
# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)       # ['banana', 'orange', 'mango']

fruits.remove('banana')
print(fruits)       # ['orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined
# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
# copying a lists

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_v2 = fruits.copy()
print(fruits_v2)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)       # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)