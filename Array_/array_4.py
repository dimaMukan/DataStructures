def large_cont_sum(arr):
    res = -999999
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                pass
            else:
                temp_res = arr[i] + arr[j]
                if temp_res >= res:
                    res = temp_res
    return res


def large_cont_sum2(arr):
    res = 0
    for i in arr:
        res = max(res+i,res)
    return res


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
print(large_cont_sum2([1,2,-1,3,4,10,10,-10,-1]))
