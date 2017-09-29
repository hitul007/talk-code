# Python 3.3

def gen1():
    yield "a"
    yield "b"
    yield "c"


def gen2():
    # for c in gen1():
    #     yield c

    yield from gen1()
    yield "d"
    yield "e"
    yield "f"
    return "RETURN VALUE"


def y_from():
    a = yield from gen2()
    print(a)


for i in y_from():
    print(i)