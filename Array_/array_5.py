def rev_word(s):
    res = ''
    s = s.split()
    for i in s[::-1]:
        res += i+' '
    return res

def rev_word1(s):
    return " ".join(reversed(s.split()))

print(rev_word('Hi John,   are you ready to go?'))
print(rev_word1('Hi John,   are you ready to go?'))