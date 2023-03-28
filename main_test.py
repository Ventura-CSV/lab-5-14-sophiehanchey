import random
import main


def test_main():

    N = 0
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 1, "Wrong number of elements"
    assert resultlst[0] == 0, "Invalid value"

    N = 5
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 6, "Wrong number of elements"
    assert resultlst[0] == 0, "Invalid value "
    assert resultlst[1] == 1, "Invalid value "
    assert resultlst[2] == 1, "Invalid value "
    assert resultlst[3] == 2, "Invalid value "
    assert resultlst[4] == 3, "Invalid value "
    assert resultlst[5] == 5, "Invalid value "


def test_fibo2():

    N = 10
    gen = main.fibo(N)
    resultlst = list(gen)
    print('Your result: ', end=' ')
    for v in resultlst:
        print(v, end=' ')
    print()

    assert len(resultlst) == 11, "Wrong number of elements"
    assert resultlst[0] == 0, "Invalid value "
    assert resultlst[1] == 1, "Invalid value "
    assert resultlst[2] == 1, "Invalid value "
    assert resultlst[3] == 2, "Invalid value "
    assert resultlst[4] == 3, "Invalid value "
    assert resultlst[5] == 5, "Invalid value "
    assert resultlst[6] == 8, "Invalid value "
    assert resultlst[7] == 13, "Invalid value "
    assert resultlst[8] == 21, "Invalid value "
    assert resultlst[9] == 34, "Invalid value "
    assert resultlst[10] == 55, "Invalid value "


def test_yield():
    with open('main.py') as f:
        flag = False
        for line in f:
            if 'yield' in line:
                flag = True
                break

    assert flag == True
