# 1) Реализуйте  генераторную  функцию,  которая  будет  возвращать  по
# одному  члену  геометрической  прогрессии  с  указанным  множителем.
# Генератор должен остановить свою работу или по достижению указанной
# границы, или при передаче команды на завершение.
import sys


def gen_geometric_progression(b, q, stop):
    while b < stop:
        tmp_b = b * q
        yield b
        if tmp_b == "stop":
            sys.exit()
        else:
            b = tmp_b
    return


g2 = gen_geometric_progression(2, 2, 100)
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
g2.send('stop')

