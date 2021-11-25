def Radix_sort(array, base=2):
    maxz = max(array)
    iter = 0
    while base ** iter < maxz:
        window = [[] for _ in range(base)]
        for i in array:
            digit = (i // (base ** iter)) % base
            window[digit].append(i)
        array = []
        for i in window:
            array.extend(i)
        iter += 1
    return array


print(Radix_sort([3, 4, 5, 1, 66, 7, 7]))
