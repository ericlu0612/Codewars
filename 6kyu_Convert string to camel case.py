def to_camel_case(text):
    lst = [s for s in text]
    for i in range(len(lst)):
        if lst[i] in ('-', '_'):
            lst[i+1] = lst[i+1].upper()
    return ''.join([i for i in lst if i not in ('-', '_')])


x = to_camel_case("a-Cat_is-evil")
print(x)
