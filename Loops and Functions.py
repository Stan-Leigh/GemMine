# 1
number = 0

while number <= 10:
    print(number)
    number += 1

# 2
start = 1
output = ''

while start <= 5:
    output += str(start) + ' '
    print(output)
    start += 1

# 3
user_input = int(input('Enter a number: '))
count = 0

while user_input > 0:
    count += user_input
    user_input -= 1

print(count)

# 4
user_table = int(input('Enter a number: '))

for number in range(1, 13):
    print(f'{number} * {user_table} = {number * user_table}')

# 5
user_digit = int(input('Enter a number: '))
print(len(str(user_digit)))

# 6
number_list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for number in number_list:
    if number > 150:
        break
    elif number % 5 == 0:
        print(number)

# 7
normal_list = [10, 20, 30, 40, 50]
reverse_list = []

for number in normal_list:
    reverse_list.insert(0, number)

print(reverse_list)

# 8
fac_number = int(input('Enter a number: '))
factorial = 1
for number in range(1, fac_number + 1):
    factorial *= number

print(factorial)

# 9
pattern_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for number in pattern_list:
    print('* ' * number)

# 10


def calculation(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2

    return f'addition = {addition}, subtraction = {subtraction}'


print(calculation(5, 6))

# 11


def showEmployee(name, salary=9000):
    return f'employee name - {name}, employee salary - {salary}'


print(showEmployee('Bolu', 8900))
print(showEmployee('Bolu'))

# 12


def calculateArea(radius, diameter):
    area = 3.14 * radius * (diameter / 2)

    return area


print(calculateArea(7, 14))
