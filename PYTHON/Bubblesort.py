def bsort(arr,a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,a-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True

a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)
bsort(arr,a)
print(arr)

