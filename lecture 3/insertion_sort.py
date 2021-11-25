def Insertion_sort(array):
    for index in range(1, len(array)):
        i = index
        while array[i] < array[i - 1] and (i - 1) >= 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


a = [4, 55, 3, 2, 8, 56, 1]
print(Insertion_sort(a))
