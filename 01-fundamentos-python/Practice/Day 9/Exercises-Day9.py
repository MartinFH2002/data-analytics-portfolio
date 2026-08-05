# Exercises Day 9
# Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
user_age = int(input('Ingresá tu edad:'))
if user_age >= 18:
    print('Usted tiene la edad suficiente para manejar')
else:
    missing_years = 18 - user_age
    print (f'A usted le faltan {missing_years} años para poder manejar')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 24
your_age = int(input('Ingresá tu edad:'))

if my_age > your_age:
    age_diff = my_age - your_age
    print (f'Yo soy {age_diff} años más grande que vos')
elif my_age < your_age:
    age_diff = your_age - my_age
    print (f'Vos sos {age_diff} años más grande que yo')
else:
    print ('Tenemos la misma edad')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = float(input('Ingresá el primer número:'))
b = float(input('Ingresá el segundo número:'))

if a > b:
    print(f'{a} es mayor que {b}')
elif a < b: 
    print(f'{a} es menor que {b}')
else:
    print('Ambos números son iguales')

# Level 2
# 1. Write a code which gives grade to students according to theirs scores:
#90-100, A
#80-89, B
#70-79, C
#60-69, D
#0-59, F
grade_number = float(input('Ingresá tu calificación:'))

if grade_number >= 90:
    grade = 'A'
    print(f'Su califición es {grade}')
elif grade_number < 90 and grade_number >= 80:
    grade = 'B'
    print(f'Su califición es {grade}')
elif grade_number < 80 and grade_number >= 70:
    grade = 'C'
    print(f'Su califición es {grade}')
elif grade_number < 70 and grade_number >=60:
    grade = 'D'
    print(f'Su califición es {grade}')
elif grade_number < 60 and grade_number >= 0:
    grade = 'F'
    print(f'Su califición es {grade}')
else:
    print ('La calificación ingresada no es válida')

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = ['Marzo','Abril', 'Mayo', 'Otoño']
winter = ['Junio', 'Julio', 'Agosto', 'Invierno']
spring = ['Septiembre', 'Octubre', 'Noviembre', 'Primavera']
summer = ['Diciembre', 'Enero', 'Febrero', 'Verano']

month = str(input('Ingresá un mes del año:')).capitalize()

if month in autumn:
    season = autumn[-1]
    print (f'El mes ingresado es de {season}')
elif month in winter: 
    season = winter[-1]
    print (f'El mes ingresado es de {season}')
elif month in spring:
    season = spring[-1]
    print (f'El mes ingresado es de {season}')
elif month in summer:
    season = summer[-1]
    print (f'El mes ingresado es de {season}')
else: 
    print('El mes ingresado no es válido')

# 3. The following list contains some fruits: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'naranja', 'mango', 'limón']
new_fruit = str(input('Ingrese una fruta:'))

if new_fruit in fruits:
    print('La fruta ya se encuentra en la lista de frutas:', fruits)
else:
    fruits.append(new_fruit)
    print('Listado de frutas:', fruits)

# Level 3

person={
'first_name': 'Martín',
'last_name': 'Herrera',
'age': 24,
'country': 'Argentina',
'is_married': False,
'skills': ['PowerBI', 'Excel', 'Python'],
'address': {
    'neighborhood': 'Mebna II',
    'block': 'F',
    'house': 4
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
keys_lt = person.keys()

if 'skills' in keys_lt:
    skills_lt = person['skills']
    skills_lenght = len(skills_lt)
    if skills_lenght % 2 == 0:
        middle = skills_lenght // 2
        print ('Las skills del medio son:',skills_lt[middle], skills_lt[middle-1])
    else:
        print ('La skill del medio es:', skills_lt[skills_lenght//2])
    if 'Python' in skills_lt:
        print('Python' in skills_lt)
    
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills_lt = person['skills']
if 'JavaScript' in skills_lt and 'React' in skills_lt:
    print('He is a front end developer')
elif 'Node' in skills_lt and 'Python' in skills_lt and 'MongoDB' in skills_lt:
    print('He is a backend developer')
elif 'React' in skills_lt and 'Node' in skills_lt and 'MongoDB' in skills_lt:
    print('He is a fullstack developer')
else:
    print('unknown title')
# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] == True and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
else:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is not married')