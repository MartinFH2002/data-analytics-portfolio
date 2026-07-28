# Excercises day 5
# Level 1

# 1) Declare an empty list
empty_list = []
print ('Lista vacía:', empty_list)

# 2) Declare a list with more than 5 items
list_5 = ['Patricia', 'Raúl', 'Amparo', 'Amalia', 'Chicha', 'Kali', 'Martín']
print ('Lista con más de 5 elementos:', list_5)

# 3) Find the length of your list
length_l5 = len(list_5)
print (f'La lista tiene en realidad {length_l5} elementos')

# 4) Get the first item, the middle item and the last item of the list
first_item = list_5[0]
middle_item = list_5 [3]
last_item = list_5 [-1]
print(f'El primer elemento de la lista es {first_item}, el elemento del medio es {middle_item} y el último elemento es {last_item}')

# 5) Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Martín', 24, 1.76, 'single', 'Barrio Mebna']
print ('Mis datos son:',mixed_data_types)

# 6) Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print('Compañías de IT:', it_companies) # 7) Print the list using print()

number_it_companies = len(it_companies) # 8) Print the number of companies in the list
print(f'Son {number_it_companies} compañías')

first_c = it_companies[0] # 9) Print the first, middle and last company
middle_c = it_companies[3]
last_c = it_companies [-1]
print(f'La primea compañía de la lista es {first_c}, la del medio es {middle_c} y la última es {last_c}')


it_companies[-2] = 'Globant' # 10) Print the list after modifying one of the companies
print('Lista de compañías IT modificada:', it_companies)

it_companies.append('Intel') # 11) Add an IT company to it_companies
print('Lista con empresa añadida:', it_companies)
it_companies.insert(4, 'Nvidia') # 12) Insert an IT company in the middle of the companies list
print('Lista con empresa insertada en el medio', it_companies)

# 13) Change one of the it_companies names to uppercase (IBM excluded!)
upper_cased_company = it_companies[1].upper()
print(upper_cased_company)
it_companies[1] = upper_cased_company
print(it_companies)

# 14) Join the it_companies with a string '#;  '
companies_joined = '#; '.join(it_companies)
print (companies_joined)

# 15) Check if a certain company exists in the it_companies list.
company_check = 'Microsoft' in it_companies
print ('¿Está Microsoft en la lista?', company_check)

# 16) Sort the list using sort() method
it_companies.sort()
print (it_companies)

# 17) Reverse the list in descending order using reverse() method
it_companies.reverse()
print (it_companies)

# 18) Slice out the first 3 companies from the list
first_3_companies = it_companies[0:3]
print (first_3_companies)

# 19) Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
print (last_3_companies)

# 20) Slice out the middle IT company or companies from the list
middle_possition = (len(it_companies) + 1)/ 2
middle_index = int (middle_possition - 1)
middle_company = it_companies[middle_index]
print (middle_company)

# 21) Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22) Remove the middle IT company or companies from the list
middle_possition = len(it_companies) / 2
middle_index1 = int (middle_possition - 1)
middle_index2 = int(middle_possition)
del it_companies[middle_index1 : middle_index2 + 1]
print (it_companies)

#  23) Remove the last IT company from the list
it_companies.pop()
print (it_companies)

# 24) Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25) Destroy the IT companies list
del it_companies

# 26) Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_and_back = front_end + back_end
print (front_and_back)

# 27) After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_and_back.copy()
Redux_index = full_stack.index('Redux')
full_stack.insert(Redux_index + 1 , 'Python')
py_index = full_stack.index('Python')
full_stack.insert(py_index + 1, 'SQL')
print (full_stack)

# Level 2

# 1) The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print (ages)
max_age = max(ages)
min_age = min(ages)
print (f'La edad más grande es {max_age} y la más chica es {min_age}')

# Add the min age and the max age again to the list
ages.append(max_age)
ages.append(min_age)
ages.sort()
print(ages)

# Find the median age (one middle item or two middle items divided by two)
print (len(ages))
middle_index1 = int ((len(ages) / 2) - 1)
middle_index2 = int (len(ages) / 2)
median_age = (ages[middle_index1] + ages[middle_index2]) / 2
print (f'The median age is {median_age}')

# Find the average age (sum of all items divided by their number )
total = sum(ages)
average_age = total / len(ages)
print(f'The avarage age is {average_age}')

# Find the range of the ages (max minus min)
range_ages = max_age - min_age
print (f'The range of the ages is {range_ages}')

# Compare the value of (min - average) and (max - average), use abs() method
min_av =  min_age - average_age
max_av = max_age - average_age
print ('Is (min - average) equal to (max - average)?', abs(min_av) == abs(max_av))
print ('Is (min - average) bigger to (max - average)?', abs(min_av) > abs(max_av))

# Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
# Intento sin IA
print (len(countries))
middle_position_countries = (len(countries) + 1) / 2
print (middle_position_countries)
middle_country_index = int(middle_position_countries - 1)
middle_country = countries[middle_country_index]
print (middle_country)

# Versión de IA (Claude): Mejor, más directa. USAR FLOOR DIVISION
middle_index = len(countries) // 2
middle_country = countries[middle_index]
print(middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[0: (middle_index + 1)]
second_half = countries[(middle_index + 1):]

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries

print(first)               # China
print(second)              # Russia
print(third)               # USA
print(scandic_countries)   # ['Finland', 'Sweden', 'Norway', 'Denmark']

# Finished