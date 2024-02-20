def tub_son(n):
    m = 0
    k = 2

    while m < n:
        if all(k % i != 0 for i in range(2, int(k ** 0.5) + 1)):
            yield k
            m += 1
        k += 1


a = int(input())
tub_generator = tub_son(a)

for number in tub_generator:
    print(number)
