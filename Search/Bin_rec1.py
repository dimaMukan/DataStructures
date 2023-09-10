def bin_rec(arr:list,item:int):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid] == item:
            return True
        else:
            if item < mid:
                return bin_rec(arr[:mid],item)
            return bin_rec(arr[mid+1:],item)
print(bin_rec([1,2,3,4,5],6))
