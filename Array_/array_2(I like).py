def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    return '\n'.join(map(str,list(output)))

print(pair_sum([1,9,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

