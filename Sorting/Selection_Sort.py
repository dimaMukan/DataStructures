def Selection_Sort(arr:list):
    for i in range(len(arr)):
        temp = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[temp]:
                temp = j
        (arr[i],arr[temp]) = (arr[temp],arr[i])



arr = [-2, 45, 0, 11, -9,88,-97, -200,747]
Selection_Sort(arr)
print(arr)

