# Exercises - Day 3
my_age = int(24)
my_height = float(1.75)
complex_number = 10 - 2j

# Triangle area calculator
t_base = float(input('Enter base of triangle: '))
t_height = float(input('Enter height of triangle: '))
t_area = 0.5 * t_base * t_height
print('The area of the triangle is: ', t_area)

# Triangle perimeter calculator
t_side1 = float(input('Enter side 1 of triangle: '))
t_side2 = float(input('Enter side 2 of triangle: '))
t_side3 = float(input('Enter side 3 of triangle: '))
t_perimeter = t_side1 + t_side2 + t_side3
print('The perimeter of the triangle is: ', t_perimeter)

# Rectangle area and perimeter calculator
r_length = float(input('Enter length of rectangle: '))
r_width = float(input('Enter width of rectangle: '))
r_area = r_length * r_width
r_perimeter = 2 * (r_length + r_width)
print('The area of the rectangle is: ', r_area)
print('The perimeter of the rectangle is: ', r_perimeter)

# Circle area and circumference calculator
number_pi = 3.14
c_radius = float(input('Enter radius of circle: '))
c_area = number_pi * c_radius ** 2
c_circum = 2 * number_pi * c_radius
print('The area of the circle is:', c_area)
print('The circumference of the circle is:', c_circum)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# slope
slope_1 = 2 #The number with next to x is the slope

# x_intercept
y = 0
x_intercept = (y + 2)/2
print('The x-intercept is:', x_intercept)

# y_intercept
x = 0
y_intercept = 2*x - 2
print('The y-intercept is:', y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

point_1 = (2 , 2)
point_2 = (6 , 10)
slope_2 = (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
distance = ((point_2[0]-point_1[0])**2 + (point_2[1]-point_1[1])**2)**0.5
print('The slope between the points is:', slope_2)
print('The Euclidean distance between the points is:', distance)

# Compare the slopes in tasks 8 and 9.
print('The slope in task 8 is:', slope_1)
print('The slope in task 9 is:', slope_2)
print('Are the slopes equal?', slope_1 == slope_2)
print('Is the slope in the task 8 higher than the slope in 9?: ' , slope_1 > slope_2)
print ('Is the slope in the task 8 lower than the slope in 9?: ' , slope_1 < slope_2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Para hacerlo bien deberíamos usar un loop, que todavía no vemos, asi que voy a probar con algunos valores de x y voy a encontrar el valor de x que hace que y sea 0 matematicamente.
x_values = [-10, -5, 0, 5, 10]
y_negten = x_values[0]**2 + 6*x_values[0] + 9
y_negfive = x_values[1]**2 + 6*x_values[1] + 9
y_zero = x_values[2]**2 + 6*x_values[2] + 9
y_five = x_values[3]**2 + 6*x_values[3] + 9
y_ten = x_values[4]**2 + 6*x_values[4] + 9
y_values = [y_negten, y_negfive, y_zero, y_five, y_ten]

print ('The x values are:', x_values)
print ('The y values for each x value are:', y_values)

# y es una función cuadrática, por lo que hay dos valores que la hacen cero.
a = 1
b = 6
c = 9
x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print ('The values of x that makes y zero are: ', x1, 'and', x2)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print (not (len_python == len_dragon))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Is "on" found in "python"?', 'on' in 'python')
print('Is "on" found in "dragon"?', 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
print('Is "jargon" found in the sentence?', 'jargon' in sentence)

# There is no 'on' in both dragon and python
print('Is "on" found in both "python" and "dragon"?', 'on' in 'python' and 'on' in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
len_python = len('python')
len_python_float = float(len_python)
len_python_string = str(len_python)
print('The length of "python" as a float is:', len_python_float)
print('The length of "python" as a string is:', len_python_string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input('Enter a number to check if it is even or not: '))
number_is_even = number % 2 == 0
print ('Is the number even?', number_is_even)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_number = int(2.7)
print ('Is the floor division of 7 by 3 equal to the int conversion of 2.7?', floor_division == int_number)

# Check if type of '10' is equal to type of 10
type_of_10_st = type('10')
type_of_10_int = type(10)
print ('Are the types of "10" and 10 the same?', type_of_10_st == type_of_10_int)

# Check if int('9.8') is equal to 10
print ('Is int("9.8") equal to 10?', int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input('Enter hours worked: '))
rate_per_hour = float(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print('The pay of the person is:', pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years_lived = int(input('Enter number of years lived: '))
seconds_lived = 365 * 24 * 60 * 60 * years_lived
print('The number of seconds a person can live is:', seconds_lived)

# Table
print ('Table')
print (1, 1**0, 1**1, 1**2, 1**3)
print (2, 2**0, 2**1, 2**2, 2**3)
print (3, 3**0, 3**1, 3**2, 3**3)
print (4, 4**0, 4**1, 4**2, 4**3)
print (5, 5**0, 5**1, 5**2, 5**3)

