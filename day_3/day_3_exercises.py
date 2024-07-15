import math

age = 22
height = 6.0
complex = 2 + 5j
# Triangle calculations
base = float(input('Please enter base: '))
height = float(input('Please enter height: '))
area = .5 * base * height
print('The area of the triangle is: ', int(area))

a = int(input('Enter side \'a\' length: '))
b = int(input('Enter side \'b\' length: '))
c = int(input('Enter side \'c\' length: '))
perimeter = a + b + c
print('The perimeter of the triangle is: ', perimeter)

# Rectangle calculations
length = int(input('Enter a length: '))
width = int(input('Enter a width: '))

rec_area = length * width
rec_perimeter = 2 * (length + width)
print('The area of the rectangle is: ', rec_area)
print('This is the perimeter of the rectangle: ', rec_perimeter)

# Circle calculations
radius = float(input("Input a Radius:"))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('Area of Circle: ',area_of_circle)
print('Circumference of Circle: ', circum_of_circle)

# Calculating slope and euclidian distance
point_a = [2,2]
point_b = [6, 10]

m = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0]) 
e_distance = math.sqrt(((point_b[0] - point_a[0])) ** 2 + ((point_b[1] - point_a[1])) ** 2)
print('This is the slope: ', m)
print('This is the euclidian distance between (2,2) and (6,10)', e_distance)

x = int(input('Enter an \'x\' value: '))
y = x ** 2 + (6*x) +9
print('Value of y = ',y)

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon.')

print('on' not in 'python' and 'on' not in 'dragon')

print(str(float(len('python'))))

num = int(input('Enter a number to see if even: '))
print((num % 2 == 0))

print((7//3) == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

# Write a script that calculates pay given rate and hours
rate = int(input('Enter rate: '))
hours = int(input('Enter hours: '))
print('Your weekly earnings is $', (rate * hours))

years = int(input('Enter the amount of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
print('You have lived for ', seconds, ' seconds.')
'''
Write a script that shows the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
print(1 ,1 ** 0, 1 ** 1, 1 ** 2, 1 ** 3)
print(2 ,2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3)
print(3 ,3 ** 0, 3 ** 1, 3 ** 2, 3 ** 3)
print(4 ,4 ** 0, 4 ** 1, 4 ** 2, 4 ** 3)
print(5 ,5 ** 0, 5 ** 1, 5 ** 2, 5 ** 3)