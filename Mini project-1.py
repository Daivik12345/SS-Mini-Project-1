from itertools import combinations


numbers = {-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}


comb = combinations(numbers, 5)


iteration = [case for case in comb if sum(case) == 0]


for subset in iteration:
    print(subset)