# Sorting Algorithm
# Bubble sort

def bubble_sort(list):
    l = len(list)
    for i in range(l-1):
        for j in range(l-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


list = [15, 2, 7, 4, 27, 19, 8]
print("sorted list -",bubble_sort(list))
