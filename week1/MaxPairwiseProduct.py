def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    maximalNumber1 = -1
    maximalNumber1Index = -1
    maximalNumber2 = -1
    for first in range(n):
        if numbers[first] > maximalNumber1:
            maximalNumber1 = numbers[first]
            maximalNumber1Index = first
    for second in range(n):
        if numbers[second] > maximalNumber2 and second != maximalNumber1Index:
            maximalNumber2 = numbers[second]
    return maximalNumber1 * maximalNumber2


from random import randint


def max_prod_stress(N, M):
    while True:
        n = randint(2, N)
        A = [None] * n
        for i in range(n):
            A[i] = randint(0, M)
        print(A)
        result1 = max_pairwise_product(A)
        result2 = max_pairwise_product_fast(A)
        if result1 == result2:
            print('OK')
        else:
            print('Wrong answer:', result1, result2)
            return


if __name__ == '__main__':
    # _ = int(input())
    # print(_)
    # input_numbers = list(map(int, input().split()))
    # print(max_pairwise_product(input_numbers))
    max_prod_stress(5, 100)
