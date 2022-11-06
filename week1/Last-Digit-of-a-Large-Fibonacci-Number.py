def last_digit_of_fibonacci_number_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    c = 0
    for i in range(2,n+1):
        c = (a + b)%10
        a = b
        b = c
    return c

 #40 102334155

print("--")
print(last_digit_of_fibonacci_number_iterative(327305))