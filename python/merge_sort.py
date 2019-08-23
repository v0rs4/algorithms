from random import shuffle

def mergeSort(arr):
    if len(arr) == 1:
        return
        
    m = len(arr) // 2

    left = arr[:m]
    right = arr[m:]

    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == "__main__":
    arr = list(range(11))
    shuffle(arr)
    print(f"Before: {arr}")
    mergeSort(arr)
    print(f"After: {arr}")