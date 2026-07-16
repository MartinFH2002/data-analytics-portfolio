# Day 2: 30 Days of python programming
# Level 1
first_name = 'Martín' #str
last_name = 'Herrera' #str
full_name = first_name + ' ' + last_name #str
country = 'Argentina' #str
city = 'Mendoza' #str
age = 24 #int
year = 2026 #int
is_married = False #bool
is_true = True #bool
is_light_on = True #bool
is_working , company_name, job_title = True, 'Valle Lindo Winery', 'Sales Administrative' #bool, str, str
#Level 2
print ('types of variables')

print(type(first_name)) #str
print(type(last_name)) #str
print(type(full_name)) #str
print(type(country)) #str
print(type(city)) #str
print(type(age)) #int  
print(type(year)) #int
print(type(is_married)) #bool
print(type(is_true)) #bool
print(type(is_light_on)) #bool
print(type(is_working)) #bool
print(type(company_name)) #str
print(type(job_title)) #str

print('Length of first_name:', len(first_name)) #6
print('Length of last_name:', len(last_name)) #7

num_one, num_two = 5, 4 
print ('number one is:', num_one, 'number two is: ', num_two)
total = num_one + num_two #9
print ('Addition: ', total)
diff = num_one - num_two #1
print ('Subtraction: ', diff)
product = num_one * num_two #20
print ('Multiplication: ', product)
division = num_one / num_two #1.25
print ('Division: ', division)
remainder = num_one % num_two #1 
print ('Remainder: ', remainder)
exp = num_one ** num_two #625
print ('Exponentiation: ', exp)
floor_division = num_one // num_two #1
print ('Floor Division: ', floor_division)

# The radius of a circle is 30 meters.
radius = 30
area_of_circle =  3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print ('radius: ', radius, 'Area: ', area_of_circle, 'Circumference: ', circum_of_circle)

radius = input ('Enter radius of a circle: ')
area_of_circle = 3.14 * float(radius) ** 2
print('Area of circle:', area_of_circle)

# User data
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')

help('keywords')

