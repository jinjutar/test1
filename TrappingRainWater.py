height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(height)
left = 0
right = n-1
leftmax = height[left]
rightmax = height[right]
res = 0
while left < right:
    if leftmax < rightmax:
        left += 1
        leftmax= max(leftmax, height[left])
        res += leftmax-height[left]
    else:
        right -= 1
        rightmax = max(rightmax, height[right])
        res += rightmax - height[right]

print(res)

