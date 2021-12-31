def gen_numbers(start, stop, step):
    while start < stop:
        yield start
        start += step
    return


g = gen_numbers(5, 10, 2)
for el in g:
    print(el)
