def Peaknumber(arr, a):
    x = a - 1
    peak = 0
    for i in range(x):
        if i == 0:
            if arr[i] > arr[i + 1] and arr[i] > arr[x]:
                peak = arr[i]
        elif 0 < i < x:
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                peak = arr[i]
        elif i == x:
            if arr[i] > arr[0] and arr[i] > arr[i - 1]:
                peak = arr[i]
    return peak

a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)

print("The given array is \n", arr)
result = Peaknumber(arr, a)
print("Peak number is", result)
