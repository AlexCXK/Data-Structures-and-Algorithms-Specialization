# def gcd(a, b):
#     if a<b:
#         a,b = b,a
#     r = a % b
#     if (r == 0):
#         return b
#     else:
#         return gcd(b, r)

def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a)
# print(gcd(28851538, 1183019))
# print(gcd(45, 210))
# print(gcd(210, 45))

