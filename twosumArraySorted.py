class Solution:
    def twoSumSorted(number: list[int], target: int):
        a = 0
        b = len(number)-1
        while a < b:
            result = number[a] + number[b]
            if result > target:
                a -= 1
            elif result < target:
                a += 1
            elif result == target:
                return print([a+1, b+1])


Solution.twoSumSorted(number=[0, 1, 2, 3, 4], target=5)




