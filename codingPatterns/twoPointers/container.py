def containerWithMostWater(height):
    maximum = 0
    i = 0
    j = len(height) - 1
    while i < j:
        width = j - i
        area = width * min(height[i], height[j])
        maximum = max(area, maximum)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return maximum


def biggestContainer(height):
    left = 0
    right = len(height) - 1
    maximum = 0
    while left < right:
        maximum = max(maximum, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        return maximum


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maximum = containerWithMostWater(height)
print(maximum)
