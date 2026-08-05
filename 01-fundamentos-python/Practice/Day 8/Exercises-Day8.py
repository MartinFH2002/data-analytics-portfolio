# Excercises Day 8

# 1. Create an empty dictionary called dog
dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Kali'
dog['color'] = 'black'
dog['breed'] = 'belgian shepherd'
dog['legs'] = 4
dog['age'] = '3 months'
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
std_dct = {"first_name":'Martín', 'last_name':'Herrera', 'gender':'male', 'age':24, 'marital status':'single', 'skills':['Power BI', 'Excel', 'Python'], 'country':'Argentina', 'city':'Mendoza', 'adress':{'hood':'Mebna II', 'block':'F', 'house':4}}
print(std_dct)

# 4. Get the length of the student dictionary
lenght_std_dct = len(std_dct)
print(f'El tamaño del diccionario del estudiante es {lenght_std_dct}')

# 5. Get the value of skills and check the data type, it should be a list
value_skills = std_dct['skills']
print(type(value_skills))

# 6. Modify the skills values by adding one or two skills
std_dct['skills'].append('English')
print(std_dct['skills'])

# 7. Get the dictionary keys as a list
std_keys = std_dct.keys()
print(std_keys)

# 8. Get the dictionary values as a list
std_values = std_dct.values()
print(std_values)

# 9. Change the dictionary to a list of tuples using items() method
sdt_dct_list = std_dct.items()
print(sdt_dct_list)

# 10. Delete one of the items in the dictionary
std_dct.pop('marital status')
print(std_dct)

# 11. Delete one of the dictionaries
del std_dct
