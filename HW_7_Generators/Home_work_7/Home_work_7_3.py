# 3) Напишите функцию-генератор, которая будет возвращать простые числа.
# Верхняя  граница  этого  диапазона  должна  быть  задана  параметром  этой
# функции.

def prime_digits(n):
    i = 2
    j = 2
    while i <= n:
        is_prime = 1
        j = 2
        while j < i:
            if i % j == 0:
                is_prime = 0
                break
            else:
                j += 1
        if is_prime == 1:
            yield i
        i += 1
    return


primes = [p for p in prime_digits(100)]
print(primes)
