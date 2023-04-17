nums = [-1, -2, 0, 1, 2, -3, 3, 4]
a = 0
b = a+1
c = len(nums)-1
nums.sort()
ans = []

for i in range(len(nums)):

    while b < c:
        result = nums[a] + nums[b] + nums[c]
        if result == 0:
            s = [nums[a], nums[b], nums[c]]
            s.sort()
            ans.append(s)
            a += 1
        elif result < 0:
            b += 1
        elif result > 0:
            c -= 1

AnswerFinal = set()
for x in ans:
    key = repr(x)
    if key not in AnswerFinal:
        AnswerFinal.add(key)
        print(x)

















