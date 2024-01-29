### Listas ###

my_list = list()
my_other_list = []
# 2 formas de crear una lista.

print(len(my_list))

my_list = [35, 34, 44, 42, 30, 27, 29, 18]
print(len(my_list))

my_other_list = [31, 1.60, "Jorge", "Reyes"]
print(len(my_other_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

age, height, name, surname = my_other_list
print(name, surname)

# Insertar elementos en la lista
print(my_other_list) # Original
my_other_list.append(1992)
print(my_other_list)

my_other_list.insert(5, "Amarillo")
print(my_other_list)

my_other_list.remove("Amarillo")
print(my_other_list)

my_other_list.pop()
print(my_other_list)

my_other_list.pop(0)
print(my_other_list)

my_new_list = my_list.copy()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[0:3])