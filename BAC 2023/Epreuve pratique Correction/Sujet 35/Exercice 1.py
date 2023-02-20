a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

def ou_exclusif (a, b):
    n = len(a)
    c = [0] * n # c = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        if a[i] == b[i]:
            c[i] = 0
        else:
            c[i] = 1
    return c
print(ou_exclusif(a, b))
