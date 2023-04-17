nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4]
k = 3


number = []
unique = []
c = []

for i in nums:
    if i not in unique:
        unique.append(i)
        c.append(nums.count(i))
        print(unique)
        print(c)

for i in range(k):
    m = max(c)
    a = c.index(m)
    number.append(unique[a])
    c[a] = -1

print(m, a, number)




