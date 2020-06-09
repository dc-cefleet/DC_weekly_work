


def myfunc(foo, bar):
    foo +=1
    bar -=1
    return [foo, bar]

print(myfunc(2, 1))

baz = myfunc
print(baz(3, 1))

item = {"func1": myfunc}

item["func1"](3, 1)