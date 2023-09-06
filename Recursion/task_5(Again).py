# def permute(s):
#     out = []
#     if len(s)==1:
#         out = [s]
#     else:
#         for i,let in enumerate(s):
#             for perm in permute(s[:i] + s[i+1:]):
#                 out += [let + perm]
#     return out
#
#
# print(permute('123'))




def permute(s):
    if int(s) < 1:
        return s
    return int(s)%10 + permute(int(s)//10)

print(permute('123'))
