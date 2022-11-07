def fibo(n):
    a = 0
    b = 1

    p = [a % 10, b % 10]

    while True:
        c = a + b
        a = b
        b = c
        p.append(c % 10)
        if p[-2] == 0 and p[-1] == 1:
            break

    p = p[:-2]
    lenPeriod = len(p)
    print(lenPeriod)
    print(p)

    # print(p)
    # print(lenPeriod)
    sum = 0
    for i in range(0,lenPeriod):
        sum +=p[i]
    times = n//lenPeriod
    num = n%lenPeriod
    sum *=num
    for i in range(0,num+1):
        sum += p[i]
    return sum%10


# def fibo(n):
    # a = 0
    # if n == 0:
    #     return 0
    #
    # b = 1
    # if n == 1:
    #     return 1
    #
    # p = [0, 1]
    # while True:
    #     c = a + b
    #     a = b
    #     b = c
    #     p.append((c) % 10)
    #     if len(p) > 59:
    #         break
    #
    # period = len(p)
    #
    # print(p)
    # print(period)
    #
    # q = n // period
    # r = n % period
    #
    # return (q * sum(p) + sum(p[:r + 1])) % 10


print(fibo(3))