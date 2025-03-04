### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n \t \tescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Jorge", "Reyes", 31
print("Mi nombre es " + name, surname + " y mi edad es " + str(age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Se recomienda, es una buena práctica.
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

# División

language_slice = language [1:]
print(language_slice)

language_slice = language [:4]
print(language_slice)

# Reverse

reverse_lenguage = language[::-1]
print(reverse_lenguage)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))