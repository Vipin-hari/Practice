def Selection(arr,a):
    
    for i in range(a-1):
        min  = i
        for j in range(i+1,a):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]


a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)
print("Given array: \n" , arr)
Selection(arr,a)
print("Sorted array: \n", arr)