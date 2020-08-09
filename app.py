
age = 20
patient_status = 'New Patient'

print(age)
print(patient_status)

colour = input('What is your favourite colour? ')

year_of_birth = input('Birth Year: ')
age = 2019 - int(year_of_birth)
print(age)
weight_pounds = input('Weight in Pounds: ')
weight_kg = int(weight_pounds) * 0.454
print('weight_kg')
print(weight_kg)
course = 'Python for Beginners'
print(course[1])
print(course[0])
print(course[0:4])
print(course[0:])
namee = 'Jennifer'
print(namee[1:-1])
first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder'
print(message)
print(len(course))
print(course.upper())
print(course.find('r'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = 10 + 3
print(x)
x -= 3
print(x)
y = (10 + 2) * 5 ** 2
print(y)
import math
print(math.ceil(2.9))

is_hot = False
is_cold = False

if is_hot:
    print("It's hot today")
    print('Drink plenty of water')
elif is_cold:
    print("It's cold today")
    print('Wear warm clothes')
else:
    print("It's a lovely day")

print('Have a great day')

price = 1000000
good_credit = True
bad_credit = False

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f'Down Payment: ${down_payment}')

high_income = False
good_credit = True
criminal_record = True

if high_income or good_credit:
    print('Eligible for Loan')

if good_credit and not criminal_record:
    print('Eligible for Loann')
else:
    print('Not eligible')


temperature = 30
print(f"Weather today: {temperature} degree celcius")
if temperature >= 30:
    print('It is a hot day')

elif temperature <= 10:
    print('It is a cold day')

else:
    print('It is pleasent today')

name = 'Ji'
if len(name) < 3:
    print('Name cannot be less than 3 characters')
elif len(name) > 50:
    print('Maximum number cannot be more than 50')
else:
    print('Name looks good')

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'K':
    converted = weight / 0.45
    print(f'Your weight is {converted} lbs')
elif unit.upper() == 'L':
    convert = weight * 0.45
    print(f'Your weight is {convert} kilos')
