def get_middle(s):
    num1 = len(s)
    if 0 < num1 < 1000:
        if num1 % 2 == 0:
            num1 = int(num1 / 2)
            y = (s[num1 - 1] + s[num1])
        else:
            y = s[num1//2]
        return str(y)


x = get_middle("WGeapuzkCdugYTBxbEO")
print(x)
