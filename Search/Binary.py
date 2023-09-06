def bin(arr,el):
    first = 0
    last = len(arr)-1
    found = False
    while first <= last and not found:
        mid = int((first + last)/2)
        if arr[mid] == el:
            found = True
        else:
            if el <= arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(bin([1,2,3,4,5],5))