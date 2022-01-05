def to_file(file_name):
    def file_decorator(f):
        def new_function(*arg, **name_args):
            result = f(*arg, **name_args)
            file = open(file_name + ".txt", "w")
            file.write(str(result))
            file.close()
            return result

        return new_function

    return file_decorator


@to_file("Practice_9_3")
def get_sum(a, b):
    return a + b


c = get_sum(1, 3)
print(c)


@to_file("List")
def get_list(n):
    return [i for i in range(n)]


print(get_list(10))
