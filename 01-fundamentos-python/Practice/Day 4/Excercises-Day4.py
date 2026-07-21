# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(strings)
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings2 = ['Coding', 'For', 'All']
result2 = ' '.join(strings2)
print(result2)

# 3. Declare a variable named company and assign it the value 'Coding For All'.
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company.strip('Coding '))

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python For Everyone to Python For All using the replace method or other methods
pfe = 'Python For Everyone'
print(pfe.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(len(company) - 1)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
letter_1_index = pfe.index('P')
letter_2_index = pfe.index('F')
letter_3_index = pfe.index('E')

print(pfe[letter_1_index] + pfe[letter_2_index] + pfe[letter_3_index])

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
letter_1_index = company.index('C')
letter_2_index = company.index('F')
letter_3_index = company.index('A')

print(company[letter_1_index] + company[letter_2_index] + company[letter_3_index])

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'

# Encontrar la posición de inicio
start = sentence.find(phrase)

# Calcular la posición de fin
end = start + len(phrase)

# Hacer el slice
resultado = sentence[start:end]
print(resultado)  # because because because

# 26 y 27 son iguales a 23 y 25

# 28. Does 'Coding For All' start with a substring Coding?
print('28. ', company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print('29. ', company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(' Coding For All'.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
print('30Daysofpython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. Python libraries
py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(py_libraries))

# 33. Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge\nI just wonder what is next')

# 34. Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print (f'The area of the circle with radius {radius} is {area} meters square')

# 36. Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
