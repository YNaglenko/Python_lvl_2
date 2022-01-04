import time

print()


def fibonacci_recursive(value):  # рекурсивная функция
    if (value == 1) or (value == 2):
        return 1
    elif value > 2:
        return fibonacci_recursive(value - 1) + fibonacci_recursive(value - 2)


start = time.time()

for i in range(35):
    fibo_rec = fibonacci_recursive(i)
    print(fibo_rec)
print('Time is: ', time.time() - start)

fibonacci_cache = {}


def fibonacci_memo():  # обемлюющая функция
    x1, x2 = 0, 1
    cach = {}

    def next_value(n):  # замыкание
        nonlocal x1, x2
        if n in cach: return cach[n]
        if n == 0:
            cach[n] = 0
        elif n == 1:
            cach[n] = 1
        else:
            x3 = x1 + x2
            x1, x2 = x2, x3
            cach[n] = x3
        return cach[n]

    return next_value


start = time.time()

fibonacci = fibonacci_memo()  # Вызов объемлющей функции
for i in range(2, 5000):
    my_fibo = fibonacci(i)  # Вызов вложенной функции (замыкания)
    print(my_fibo)
print('Time is: ', time.time() - start)
