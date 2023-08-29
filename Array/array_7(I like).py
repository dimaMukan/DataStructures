def uni_char(s):
    a = ''.join(sorted(set(s)))
    if a == s:
        return True
    return False

print(uni_char('abcde'))

