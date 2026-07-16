# Exercise: Level 2
# Operaciones
print(3+4) # Addition
print(3-4) # Subtraction
print(3*4) # Multiplication
print(3/4) # Division
print(3**4) # Exponentiation
print(3%4) # Modulus
print(3//4) # Floor Division

# Strings
print("Martín") #name
print("Herrera") #last name
print("Argentina") #country
print("I am enjoying 30 days of python") #statement

# Checking data types
print(type(10)) # Int
print(type(9.8)) # Float
print(type(3.14)) # Pi
print(type(4-4j)) # Complex number
print(type['Asabeneh','Python','Finland']) # List
print(type('Martín')) # String
print(type('Herrera')) # String
print(type('Argentina')) # String

# Exercise: Level 3
#Examples of different data types
print(10) #Int
print(9.8) #Float
print(3+4j) #Complex number
print('Martín Herrera') #String
print(False) #Boolean
print([1, 2, 3, 4]) #List
print(('Martín', 'Herrera', 'Argentina')) #Tuple
print({'name':'Martín', 'country':'Argentina'}) #Dictionary 
print({9.8, 3.14, 2.7}) #Set

# Find the euclidean distance between the points (2, 3) and (10, 8)
point1 = (2, 3) 
point2 = (10, 8)

distancex = point2[0] - point1[0] #Distancia entre las coordenadas x
distancey = point2[1] - point1[1] #Disrancia entre las coordenadas y
distance = (distancex**2 + distancey**2)**0.5 #Distancia entre dos puntos.
print("The euclidean distance between the points (2, 3) and (10, 8) is:", distance) #Muestra el resultado
