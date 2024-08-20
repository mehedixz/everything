# Sorting algorithm
# Selection sort

def selection_sort(list):
    l = len(list)

    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp

    return list


list = [8, 5, 7, 3, 6, 2, 4, 1]
print("Sorted list -",selection_sort(list))

