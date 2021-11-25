def merge(array1, array2):
    output_array = []
    array1_traverse = 0
    array2_traverse = 0
    while array1_traverse < len(array1) and array2_traverse < len(array2):
        if array1[array1_traverse] <= array2[array2_traverse]:
            output_array.append(array1[array1_traverse])
            array1_traverse += 1
        else:
            output_array.append(array2[array2_traverse])
            array2_traverse += 1
    while array1_traverse < len(array1):
        output_array.append(array1[array1_traverse])
        array1_traverse += 1
    while array2_traverse < len(array2):
        output_array.append(array2[array2_traverse])
        array2_traverse += 1
    return output_array


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


a = [4, 55, 3, 2, 8, 56, 1]
print(merge_sort(a))
