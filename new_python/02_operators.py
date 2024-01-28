### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(3 // 4)
print(2 ** 3)

# Todo lo que se puede hacer con los operadores, trabajando con string y enteros.

print("Hola " + "Python")
print("Jorge Reyes, nació en: " + str(1992))
print("Hola " * 5)
print("Hola " *  (2 ** 2 + 2))

# Considerar que no se puede operar string y float.
# print("Hola " * 2.5) # Se produce un error.

# my_float = 2.6 * 2
# print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4) # False
print(3 != 4) # True


print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" <= "Hola")
print("Hola" >= "Zola") # Ordenación alfabética
print(len("aaaaa") >= len("bbbb")) # Cuenta caracteres
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python") # Compara.
print(not(3 > 4))

print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)