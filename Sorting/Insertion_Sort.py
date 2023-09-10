def insert_sort(arr):
    for i in range(1,len(arr)):
        cur_item = arr[i]
        pos = i
        while pos > 0 and arr[pos-1]>cur_item:
            arr[pos] = arr[pos-1]
            pos = pos-1

        arr[pos] = cur_item


a = [5,4,3,2,1]
insert_sort(a)
print(a)
