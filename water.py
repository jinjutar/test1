height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left, right, answer = 0, len(height)-1, 0
while left <= right:
    area = min(height[right], height[left])*(right-left)
    answer = max(answer, area)
    if height[right] > height[left]:
        left += 1
    else:
        right -= 1
print(answer)





