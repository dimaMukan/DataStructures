import math
def Bin_Rec(arr,el):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == el:
            return True
        else:
            if el < arr[mid]:
                return Bin_Rec(arr[:mid], el)
            else:
                return Bin_Rec(arr[mid + 1:], el)

print(Bin_Rec([1,2],7))