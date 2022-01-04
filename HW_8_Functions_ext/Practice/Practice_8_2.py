# 2) Используя функцию замыкания реализуйте такой прием программирования
# как Мемоизация - https://en.wikipedia.org/wiki/Memoization
# Используйте  полученный  механизм  для  ускорения  функции  рекурсивного
# вычисления n — го члена ряда Фибоначчи. Сравните скорость выполнения с
# просто рекурсивным подходом.

import time


def f_by_recursion(value):
    if (value == 1) or (value == 2):
        return 1
    elif value > 2:
        return f_by_recursion(value - 1) + f_by_recursion(value - 2)


start_at = time.time_ns()
for i in range(35):
    print(i, '->', f_by_recursion(i))
end_at = time.time_ns()
print('Elapsed time: ', (end_at - start_at), "nsec", i, "members")


def fib_memoization():
    mem_cache = {0: 0, 1: 1}

    def fib_member(n):
        if n in mem_cache:
            return mem_cache[n]
        else:
            mem_cache[n] = fib_member(n - 1) + fib_member(n - 2)
            return mem_cache[n]

    return fib_member


start_at = time.time_ns()
memoization_test = fib_memoization()
for i in range(35):
    f_member = memoization_test(i)
    print(i, '->', f_member)
end_at = time.time_ns()
print('Elapsed time: ', (end_at - start_at), "nsec", i, "members")
