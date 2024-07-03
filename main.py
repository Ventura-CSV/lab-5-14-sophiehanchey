def fibo(N):
    n1 = 0
    n2 = 1
    yield n1, n2
    c = 0
    while c <= N:
        n3 = n1 + n2
        yield n3
        n1 = n2
        n2 = n3
        c += 1

def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
    #     print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
