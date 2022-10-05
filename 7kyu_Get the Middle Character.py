def get_middle(s):
    num1 = len(s)
    if 0 < num1 < 1000:
        if num1 % 2 == 0:
            num1 = int(num1 / 2)
            y = (s[num1 - 1] + s[num1])
        else:
            y = s[num1//2]
        return str(y)


# def get_middle(s):
#     if len(s) == 1:
#         return s
#     if len(s) == 2:
#         return s
#     if len(s) % 2 == 0:
#         return str(s[int(len(s)/2)-1]) + str(s[int(len(s)/2)])
#     return s[int((len(s) - 1)/2)]


x = get_middle("WGeapuzkCdugYTBxbEO")
print(x)
