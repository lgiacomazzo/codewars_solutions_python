from math import ceil


def get_prime_numbers(number):
    if number < 0:
        number = -number

    prime_numbers = []
    # print("New number: " + str(number))
    for i in range(2, number // 2 + 1):
        # print(number, " : ", i)
        if number % i == 0:
            # print("Found prime number: " + str(i))
            prime_numbers.append(i)
            while number % i == 0:
                # print(str(number) + " is still divisible by " + str(i))
                number //= i
        elif number < i:
            break
    if number != 1:
        prime_numbers.append(number)
    return prime_numbers


def sum_for_list(lst):
    list_prime_numbers = []
    for elem in lst:
        list_prime_numbers += get_prime_numbers(elem)
    list_prime_numbers = sorted(frozenset(list_prime_numbers))

    return_list = []
    for factor in list_prime_numbers:
        sum_of_numbers = 0
        for elem in lst:
            if elem % factor == 0:
                sum_of_numbers += elem
        return_list.append([factor, sum_of_numbers])
    return return_list
