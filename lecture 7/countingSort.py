def counting_sort(array):
    limit = max(array)
    checklist = [0 for _ in range(limit + 1)]
    for i in array:
        checklist[i] += 1
    output = []
    for i in range(len(checklist)):
        while checklist[i] != 0:
            output.append(i)
            checklist[i] -= 1

    return output
