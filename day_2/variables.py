import math
# Day 2: 30 Days of Python Programming
first_name = 'Evan'
last_name = 'Izenstark'
full_name = first_name + " " + last_name
country = 'United States'
city = 'Chicago'
age = 22
year = 2024
is_married = False
is_light_on = True
travelling, on_plane, airport = True, True, 'PUJ'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(travelling))
print(type(on_plane))
print(type(airport))
print(len(first_name))
print(len(first_name) + len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Radius of Circle Drill
r = 30.0
area_of_circle = 3.14 * (r ** 2.0)
circum_of_circle = 2 * 3.14 * r

radius = float(input("Input a Radius:"))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('Area of Circle: ',area_of_circle)
print('Circumference of Circle: ', circum_of_circle)

# Asking user for inputs

first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
country = input('Please enter your country of residency:')
age = input('Please enter your age:')
