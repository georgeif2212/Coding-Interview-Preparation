def flipAndInvertImage(image):
    for array in image:
        for index in range(len(array)):
            array[index] = 1 if array[index] == 0 else 0
    return image


def flipAndInvertImageXOR(image):
    for array in image:
        array.reverse()
        for index in range(len(array)):
            array[index] = array[index] ^ 1
    return image


def flipAndInvertImageTwoPointers(image):
    n = len(image[0])
    for row in image:
        i, j = 0, n - 1
        while i <= j:
            # Swap + invert en un solo paso
            row[i], row[j] = row[j] ^ 1, row[i] ^ 1
            i += 1
            j -= 1
    return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

print(flipAndInvertImage(image))
print(flipAndInvertImageXOR(image))
