height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(height)
left = 0
right = n-1
leftvalue = height[left]
rightvalue = height[right]
B = []
res = 0
while left < right:
    if leftvalue < rightvalue:
        left += 1
        leftvalue = max(leftvalue, height[left])
        water = leftvalue-height[left]
        res += water
        B.append(water)

    else:
        right -= 1
        rightvalue = max(rightvalue, height[right])
        water = rightvalue - height[right]
        res += water
        B.append(water)

print(res)
print(B)

