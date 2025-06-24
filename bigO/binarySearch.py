def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(mid, arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


arr = [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#      0  1  2  3  4   5   6   7   8   9   10
print(binary_search(arr, 5))


# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#  l               m                    r
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#  l            r
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#  l     m      r                    
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#  l  r  
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
# l,m  r                      
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#  m l,r                      
# [3, 5, 7, 9, 12, 30, 34, 45, 47, 78, 89]
#   l,m,r                      