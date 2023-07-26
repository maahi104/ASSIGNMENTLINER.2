
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = input("Enter the array (space-separated): ").split()
arr = [int(i) for i in arr]

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)