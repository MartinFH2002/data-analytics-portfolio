# Excercises Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
# 1. Find the length of the set it_companies
lenght_it_companies = len(it_companies)
print(f'El tamaño del set de compañías IT es {lenght_it_companies}')

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companiescl
more_companies = ['Globant', 'Intel', 'Starlink']
it_companies.update(more_companies)
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.discard('Intel')
print (it_companies)

# 5. What is the difference between remove and discard
# La diferencia es que si usamos el método remove y el elemento no está en el ser, nos va a dar error, en cambio el método discard no.

# Level 2
# 1. Join A and B
C = A.union(B)
print(f'La unión entre A y B es {C}')

# 2. Find A intersection B
I = A.intersection(B)
print (f'La intersección entre A y B es {I}')

# 3. Is A subset of B?
print ('Is A subset of B?', A.issubset(B))

# 4. Are A and B disjoint sets
print ('Are A and B disjoint sets?', A.isdisjoint(B))

# 5. Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print(f'La unión de A y B es: {A_B}')
print(f'La unión de B y A es: {B_A}')

# 6. What is the symmetric difference between A and B
SD_A_B = A.symmetric_difference(B)
print (f'La diferencia simétrica entre A y B es: {SD_A_B}')

# 7. Delete the sets completely
del A
del B

# Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
lenght_lt = len(age)
lenght_st = len(age_st)
print (f'Is the age list bigger than the age set? {lenght_lt > lenght_st}')

# 2. Explain the difference between the following data types: string, list, tuple and set
# String: es un conjunto de caracteres, palabras básicamente.
# Lista: es un conjunto ordenado y modificable que puede contener distintos tipos de datos.
# Tupla: es un conjunto ordenado e inmutable que puede contener distintos tipos de datos.
# Set: es un conjunto desordenado y sín índice de datos. No permite elementos repetidos.

# 3. I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_lt = sentence.split()
sentence_st = set(sentence_lt)
num_of_words = len(sentence_st)
print (f'There have been used {num_of_words} words in the sentence')
