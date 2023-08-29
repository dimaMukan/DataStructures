def compress(s):
    res = set()
    tot = ''

    for i in s:
        res.add(i)

    for i in res:
        tot += i + str(s.count(i))
    return tot

def compress1(s):
    res = ''
    for i in sorted(set(s)):
        res += i + str(s.count(i))
    return res


print(compress('AAAAABBBBCCCC'))
print(compress1('AAAAABBBBCCCC'))