import random
import time
from functools import wraps


def timeit(func):
    """Выполнить функцию 'func' с параметрами '*args', '**kwargs' и
    вернуть время выполнения в мс."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        return (time_end - time_start) * 1000

    return wrapper


def n_pow_2(data):
    """Вернуть 'True', если все значения 'data' различны.

    Алгоритм 1:
      Пробежимся по списку с первого до последнего элемента и для каждого из
      них проверим, что такого элемента нет в оставшихся справа элементах.

    Сложность: O(N^2).
    """
    for i in range(len(data)):       # O(N)
        if data[i] in data[i+1:]:    # O(N) - срез + in: O(N) + O(N) = O(N)
            return False             # O(1) - в худшем случае не выполнится
    return True                      # O(1)


def n_log_n(data):
    """Вернуть 'True', если все значения 'data' различны.

    Алгоритм 2:
      Отсортируем список. Затем, если в нем есть повторяющиеся элементы, они
      будут расположены рядом — т.о. необходимо лишь попарно их сравнить.

    Сложность: O(N Log N).
    """
    copy = list(data)                # O(N)
    copy.sort()                      # O(N Log N) - «быстрая» сортировка
    for i in range(len(data) - 1):   # O(N) - N-1, округлим до O(N)
        if copy[i] == copy[i+1]:     # O(1) - [i] и ==, оба по O(1)
            return False             # O(1) - в худшем случае не выполнится
    return True                      # O(1)


def n(data):
    """Вернуть 'True', если все значения 'data' различны.

    Алгоритм 3:
      Создадим множество из списка, при создании автоматически удалятся
      дубликаты если они есть. Если длина множества == длине списка, то
      дубликатов нет.

    Сложность: O(N).
    """
    _set = set(data)                # O(N)
    return len(_set) == len(data)   # O(1) - 2 * len (O(1)) + == O(1)


if __name__ == '__main__':
    s = 5
    funcs = [n, n_log_n, n_pow_2]
    [print(f'{func.__name__:>{s + 3}} |', end=' ') for func in funcs]
    print()
    for size in (10 ** j for j in range(s)):
        sample = random.sample(range(-10 ** s, 10 ** s), size)
        for func in funcs:
            print(f'{timeit(func)(sample):>{s + 3}.2f} |', end=' ')
        print(size)
