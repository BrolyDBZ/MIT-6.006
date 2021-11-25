def MaxHeapify(array, i):
    left_child = 2 * i + 1
    right_chld = 2 * i + 2
    largest = i
    if left_child < len(array) and array[i] < array[left_child]:
        largest = left_child
    if right_chld < len(array) and array[largest] < array[right_chld]:
        largest = right_chld
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        MaxHeapify(array, largest)


def buildHeap(array):
    for i in range(len(array) // 2, -1, -1):
        MaxHeapify(array, i)


def remove(array, i=0):
    array[i], array[len(array) - 1] = array[len(array) - 1], array[i]
    output = array[len(array) - 1]
    del (array[len(array) - 1])
    MaxHeapify(array, i)
    return output


def Heapsort(array):
    buildHeap(array)
    sorted = []
    while len(array) > 0:
        sorted.append(remove(array))
    return sorted


a = [4, 53, 5, 5, 65, 4, 456, 3, 2, 66]
b = Heapsort(a)
print(b)
