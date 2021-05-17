def exp_sum(n):
    table = {}
    for i in range(n + 1):
        table[i] = {}
        for j in range(n + 1):
            table[i][j] = 0

    def _exp_sum(r_sum, l_number):
        if l_number == 0:
            return 0
        if r_sum == 0:
            return 1
        if r_sum < 0:
            return 0

        if table[r_sum][l_number] != 0:
            return table[r_sum][l_number]
        table[r_sum][l_number] = _exp_sum(r_sum, l_number - 1) + _exp_sum(r_sum - l_number, l_number)
        return table[r_sum][l_number]

    result = _exp_sum(n, n)
    return result
