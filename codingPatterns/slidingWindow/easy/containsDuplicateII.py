def containsNearbyDuplicate(nums, k):
    window = set()

    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)

        # Mantener la ventana de tamaño máximo k
        if len(window) > k:
            window.remove(nums[i - k])

    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))
