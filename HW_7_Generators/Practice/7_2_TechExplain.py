name1 = ["John", "Anna", "Andrey", "Alexander", "Alina", "Smith", "Irina"]


def get_name_part(names, n):
    index = 0
    while index < len(names):
        temp_names = []
        for i in range(index, index + n):
            if i >= len(names):
                index = i
                yield temp_names
                return
            else:
                temp_names.append(names[i])
                index = i
        index += 1
        yield temp_names
    return


names_generator = get_name_part(name1, 4)
for n in names_generator:
    print(n)
