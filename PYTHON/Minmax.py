def minmax(arr):
    arr = sorted(arr)
    min = arr[0]
    max = arr[a-1]
    print(arr)
    print(min ,"\n", max)
a = int(input())
arr = []
for i in range(a):
    b = int(input())
    arr.append(b)

print("The given array is \n", arr)
minmax(arr)