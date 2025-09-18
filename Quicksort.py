def pivoting_median_of_three_right_side(arr,left,right):
    if len(arr)>=3:
        low,mid,high = left,(left + right) // 2,right
        a,b,c = arr[low],arr[mid],arr[high]
        if (a <= b <= c) or (c <= b <= a):
            arr[high],arr[mid] = arr[mid],arr[high]
        elif (b <= a <= c) or (c <= a <= b):
            arr[high],arr[low] = arr[low],arr[high]

def partition(arr,left,right):
    pivot = arr[right]
    i = left - 1
    for j in range(left,right):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1],arr[right] = arr[right],arr[i + 1]
    return i + 1

def quicksort(arr,left,right):
    if left < right:
        pivoting_median_of_three_right_side(arr,left,right)
        pivot_index = partition(arr,left,right)
        quicksort(arr,left,pivot_index - 1)
        quicksort(arr,pivot_index + 1,right)

arr = list(map(int,input("Enter the array elements separated by space: ").split()))
quicksort(arr,0,len(arr) - 1)
print(arr)