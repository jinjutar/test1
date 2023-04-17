import math
import itertools


nums = [-1, 0, 1, 2, -1, -4]
result = 0
choose = 3


class solution:
    def problem(nums, result, choose):
        itertools.combinations(nums, choose)
        A = list(itertools.combinations(nums, choose))
        print(A)

        for i in A:
            j = sum(i)

            if j == result:
                print(i)


solution.problem(nums, result, choose)