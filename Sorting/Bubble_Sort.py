def buble_sort(arr:list):
    for i in list(range(len(arr)-1,0,-1)):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [5,4,3,2,1]
print(buble_sort(arr))