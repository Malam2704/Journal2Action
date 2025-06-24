def fib_gen(x):
    if x < 1:
        return "Invalid"
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        arry = []
        a = 0
        b = 1
        arry.append(a)
        arry.append(b)
        for i in range(0, x-2):
            arry.append(a + b)
            tempa = a
            tempb = b
            b = tempa+b
            a = tempb
        return arry


print(fib_gen(10))
