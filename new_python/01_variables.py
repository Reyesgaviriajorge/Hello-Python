# Variables

my_string_variables = "My String variable"
print(my_string_variables)
print(f'String Variable: {my_string_variables}')  # Output: String

my_int_variable = 1992
my_bool_variable = False

# Concatenación de variables en un print
print(my_string_variables, my_int_variable, my_bool_variable)

print(type(print(my_string_variables))) # Tipo 'NoneType'

# Algunas funciones:
print(len(my_string_variables))

# Variables en una sola línea:
name, surname, alias, age = "Jorge", "Reyes", "Reyesgaviriajorge", 31
print("Me llamo:", name, surname,". My edad es:", age, "Y mi alias es:", alias)

# Inputs

first_name = input("What is your name? ")
age = input("How old are you? ")

print(first_name)
print(age)

# Forzamos el tipo: No aplica en python
address: str = "Mi dirección"
address = 31
print(address)
print(type(address))