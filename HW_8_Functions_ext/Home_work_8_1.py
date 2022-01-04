def gen_func(b: int, stop: int) -> int:
    """Function calculates next member of progression, logic of calculation next member
    realized in the user defined function 'next_value'"""
    i = 0

    def next_value():
        nonlocal b
        b = (b + 1) * 2
        return b

    while i < stop:
        new_value = 0
        tmp_b = (yield next_value())
        if tmp_b == 'stop':
            exit()
        else:
            new_value = tmp_b
        i = i + 1
    return new_value


g2 = gen_func(2, 2)

print(next(g2))  # (2 + 1) * 2 = 6
print(next(g2))  # (6 + 1) * 2 = 14
g2.send('stop')
print(next(g2))
