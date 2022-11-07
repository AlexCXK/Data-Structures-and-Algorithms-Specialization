def fibo(n, m):
    a = 0
    b = 1

    p = [a % m, b % m]

    while True:
        c = a + b
        a = b
        b = c
        p.append(c % m)
        if p[-2] == 0 and p[-1] == 1:
            break

    p = p[:-2]
    lenPeriod = len(p)

    # print(p)
    # print(lenPeriod)
    print(p)
    return p[n % lenPeriod]

a= [1,2,3,4,5]
print(sum(a[1:3]))