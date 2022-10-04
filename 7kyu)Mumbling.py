# 我的解法
def accum(s):
    acc = []
    j = 0
    for i in s:
        j += 1
        for l in range(j, j+1):
            acc.append(i*l)

    acc = "-".join(acc)
    return acc.title()

"""====================================================="""
# 網路解法一
# def accum(s):
#     return '-'.join([str(s[i]*(i+1)).capitalize() for i in range(len(s))])

"""====================================================="""
# 網路解法二
# def accum(s):
#     c = 1
#     string = ''
#     for letter in s:
#         temp = (c * s[c-1])
#         temp = temp.capitalize()
#         temp = temp + '-' #append hyphen
#         string = string + temp   #append mini string to another string
#         c+= 1
#     string = string[:-1] #remove last hyphen
#     return string
"""====================================================="""


x = accum("abcdefgh")
print(x)