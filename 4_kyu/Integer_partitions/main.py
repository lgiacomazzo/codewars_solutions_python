from tests.tests import tests


# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b

cache_memory = {}


def get_from_cache(max_number, residual_sum):
    """
    Access cache_memory and recover the list associated to both parameters
    :param max_number: First element of a partition
    :param residual_sum: Sum of elements in a partition
    :return: a list containing one partition only
    """
    if max_number not in cache_memory:
        return None
    if residual_sum not in cache_memory[max_number]:
        return None
    return cache_memory[max_number][residual_sum]


def add_to_cache(max_number, residual_sum, result_list):
    """
    Stores inside cache_memory a partition associated to both parameters
    :param max_number: First element of a partition
    :param residual_sum: Sum of elements in a partition
    :param result_list: a list containing one partition only
    """
    if max_number not in cache_memory:
        cache_memory[max_number] = {}
    if residual_sum not in cache_memory[max_number]:
        cache_memory[max_number][residual_sum] = result_list


def _enum(max_number, residual_sum):
    """
    It recursevely generates a list of partitions that start with max_number and that sum up
    to residual_sum. Uses cache_memory for fast storage and retrieval of already computed
    partitions.
    :param max_number: First element of a partition
    :param residual_sum: Sum of elements in a partition
    :return: a list containing one or more lists, each one containing a partition
    """
    result_list = []
    if residual_sum <= 0:
        return result_list
    residual_sum -= max_number
    if residual_sum > 0:
        if get_from_cache(max_number, residual_sum) is not None:
            return get_from_cache(max_number, residual_sum)
        for new_max_number in range(max_number, 0, -1):
            for single_list in _enum(new_max_number, residual_sum):
                single_partition = [max_number] + single_list
                result_list.append(single_partition)
        add_to_cache(max_number, residual_sum, result_list)
    elif residual_sum == 0:
        result_list.append([max_number])
    return result_list


def enum(num):
    """
    It recovers partitions associated with num. It's based on the principle that all partitions
    start with a number going from num to 1 called max_number, and all numbers inside a partition
    are lower or equal than max_number. There may be multiple partitions associated with a
    max_number. Uses cache_memory for fast storage and retrieval of already computed partitions.
    :param num: number on which partitions are computed
    :return: list of lists, each one containing a partition of num
    """
    if get_from_cache(num, 0) is not None:
        return get_from_cache(num, 0)
    result_list = []
    for max_number in range(num, 0, -1):
        for single_list in _enum(max_number, num):
            result_list.append(single_list)
    add_to_cache(num, 0, result_list)
    return result_list


def part(num):
    """
    Recovers all partitions of num, and computes range, mean, and median.
    :param num: number used for computing partitions
    :return: a string formatted for printing containing range, mean, median
    """
    result_list = enum(num)
    result_list_products = set()
    for sub_list in result_list:
        result = 1
        for elem in sub_list:
            result *= elem
        result_list_products.add(result)
    products_sorted = list(sorted(result_list_products))
    range_products = products_sorted[-1] - products_sorted[0]
    mean = sum(products_sorted) / len(products_sorted)
    # since each index starts from 0, all indexes computed must be shifted by 1
    # example: if len == 3, ([0, 1, 2]) --> 1 == (len // 2)
    # example: if len == 4, ([0, 1, 2, 3]) --> (1 + 2) / 2 == (((len//2-1) + (len//2)) / 2)
    if len(products_sorted) % 2 == 1:
        median = products_sorted[len(products_sorted) // 2]
    else:
        median = (products_sorted[len(products_sorted) // 2 - 1] +
                  products_sorted[len(products_sorted) // 2]) \
                 / 2
    return "Range: {range} Average: {mean:.2f} Median: {median:.2f}"\
        .format(range=range_products, mean=mean, median=median)


def test():
    """
    Test method
    """
    for arg, result in tests:
        result_func = part(arg)
        print("arg:", arg, ", result desired:", result, ", result obtained:", result_func)
        if result_func != result:
            raise Exception("Test not passed")
        print("---------------------------------")
    print("Tests passed")


if __name__ == '__main__':
    test()
