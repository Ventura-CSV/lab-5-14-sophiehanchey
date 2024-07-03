def fibo(N):
    # define values for start and incrementation
    c = 0
    n1 = 0
    n2 = 1
    while c <= N:
        if c == 0:
            yield 0
        elif c == 1:
            yield 1
        else:
            n3 = n1 + n2
            yield n3
            
            # update fibbonacci specific values
            n1 = n2
            n2 = n3
            
        # update overall count
        c += 1   
            
            
def main():
    N = 16
    gen = fibo(N)
    # for v in gen:
         #print(v, end=' ')
    print(list(gen))


if __name__ == '__main__':
    main()
