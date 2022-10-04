def order(sentence):
    lst = []
    for i in range(1, 10):
        for j in sentence.split():
            if str(i) in j:
                lst.append(j)
    return " ".join(lst)


# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: list(filter(str.isdigit, x))[0]))
x = order("is2 Thi1s T4est 3a")
print(x)
