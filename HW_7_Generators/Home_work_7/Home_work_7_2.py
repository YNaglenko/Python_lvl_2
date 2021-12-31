# 2)  Реализуйте  свой  аналог  генераторной  функции  range()
def gen_range(start, stop, step=None):
    step = 1 if step is None else step
    while start < stop:
        yield start
        start += step
    return


a = [num for num in gen_range(1, 10)]
print(a)

b = [num for num in gen_range(1, 30, 3)]
print(b)
