
names = ["Guilherme", "Gabriel", "Davi"]
# print(nmes)

# for name in names:
#     print(name.upper()) 

# if "Guilherme" in names:
#     names.remove("Gabriel")

#     names.insert(3, "Robinho")
#     names.append("Gabriel")
#     print(names)

names2 = ["Maria","Julia","Carol"]
names.extend(names2)

# print(names) - ['Guilherme', 'Gabriel', 'Davi', 'Maria', 'Julia', 'Carol']


def upper_list(lista):
    newList = [item.upper() for item in lista]
    return newList

list_of_names = ["gui","biel","davi"]
upper_list(list_of_names)
# print(list_of_names)

