func_array = []


def decorator_reg_function(func):
    func_array.append(func)
    return func


@decorator_reg_function
def get_sum(a, b):
    return a + b


@decorator_reg_function
def get_mul(a, b):
    return a * b


@decorator_reg_function
def get_double(a):
    return a * 2


for f in func_array:
    print(f)
