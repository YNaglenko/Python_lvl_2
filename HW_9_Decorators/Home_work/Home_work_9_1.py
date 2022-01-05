# 1) Создайте  декоратор,  который  будет  подсчитывать,  сколько  раз  была
# вызвана декорируемая функция.


class CountCallsDecorator:
    def __init__(self, func):
        self.func = func
        self.count_calls = 0

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.count_calls += 1
        return result


@CountCallsDecorator
def multiply(a, b):
    return a * b


print(multiply(2, 1))
print(multiply(2, 2))
print(multiply(2, 3))
print(multiply(2, 4))
print(multiply(2, 5))

print("Count of calls:", multiply.count_calls)
