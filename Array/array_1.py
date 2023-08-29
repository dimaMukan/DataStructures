def anagram(s1:str, s2:str):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    return sorted(s1) == sorted(s2)

print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
