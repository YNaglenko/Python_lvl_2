# # 4) Создайте декоратор с параметрами для проведения хронометража работы
# # той или иной функции. Параметрами должны выступать то, сколько раз нужно
# # запустить  декорируемую  функцию  и  в  какой  файл  сохранить  результаты
# # хронометража. Цель - провести хронометраж декорируемой функции.
#
import time


def timing_log_iterations(q_iteration, file_name):
    i = 0

    file = open(str(file_name) + ".txt", "a+")
    start_time = time.time()
    while i < q_iteration:
        def logger(func):
            def new_func(*args, **kwargs):
                f_work = func(*args, **kwargs)
                return f_work
            return new_func

        i = i + 1
    end_time = time.time()
    elapsed = (end_time - start_time)
    file.write(
        "Function done {} iteration(s) for elapsed time: {} seconds \n".format(q_iteration, elapsed))
    file.close()
    return logger


@timing_log_iterations(5, "Test_9_4_10")
def f_by_recursion(value):
    if (value == 1) or (value == 2):
        return 1
    elif value > 2:
        return f_by_recursion(value - 1) + f_by_recursion(value - 2)


res = f_by_recursion(39)
print(res)
