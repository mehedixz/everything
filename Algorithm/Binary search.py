# Search algorithm
# Binary search
def binary_search(l, x):
    left = 0
    right = len(l)

    while left <= right:
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            left = mid+1
        else:
            right = mid-1

    return 'not found'


l = [2, 4, 8, 9, 11, 13, 29, 35, 57, 61, 73, 81]
x = int(input("Enter your finding number : "))
print(binary_search(l, x))

