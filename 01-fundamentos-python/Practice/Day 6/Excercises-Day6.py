# Excercises Day 6
# Level 1

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters_tuple = ('Amparo',)
brothers_tuple = ('Tomás', 'Martiniano')
print ('Hermanas:', sisters_tuple)
print ('Hermanos:', brothers_tuple)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings_tuple = sisters_tuple + brothers_tuple
print ('Hermanos y hermanas:', siblings_tuple)

# 4. How many siblings do you have?
number_siblings = len(siblings_tuple)
print (f'Tengo {number_siblings} hermanos y hermanas')

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings_tuple + ('Raúl', 'Patricia')
print ('Mi familia:', family_members)

# Level 2

# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print ('Hermanos y hermanas:', siblings)
print ('Padres:', parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'naranja', 'manzana', 'mandarina')
vegetables = ('lechuga', 'tomate', 'cebolla', 'pimiento')
animal_products = ('leche', 'carne', 'huevos')
food_stuff_tp = fruits + vegetables + animal_products
print ('Alimentos:', food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[middle_index]
print ('Elemento del medio:', middle_items)

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print ('Primeros tres elementos:', first_three_items)
print ('Últimos tres elementos:', last_three_items)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
print (f'¿Estonia es un país nórdico? {is_estonia_nordic}')

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print (f'¿Islandia es un país nórdico? {is_iceland_nordic}')

