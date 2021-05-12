import math

# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations


class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {0: 1, 1: 1}

    def __call__(self, n):
        if n < 0:
            return 0
        if n not in self.cache:
            self.cache[n] = self.func(n)
        return self.cache[n]


def compute_range(n):
    square_root = math.sqrt(24 * n + 1)
    return range(int(-(square_root - 1) / 6), int((square_root + 1) / 6) + 1)


@Memoize
def exp_sum(n):
    number_partitions = 0
    for k in compute_range(n):
        if k == 0:
            continue
        p = exp_sum(n - k * (3 * k - 1) // 2)
        if p == 0:
            break
        elif k % 2 == 0:
            p = -p
        number_partitions += p
    return number_partitions
