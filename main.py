def fibo(N):
    # define n1 and n2
    n1 = 0
    n2 = 1
    
    #yield n1 and n2
    yield n1
    yield n2
    
    # generate remainder of fibonacci sequence
    c = 0
    while c <= N-2:
        n3 = n1 + n2
        yield n3
        
        # update values
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
