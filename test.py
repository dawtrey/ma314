global x
x = 0
def f():
    print(g())
    print(x)

def g():
    while x != 10:
        x += 1
        print(x)
    return x


f()
