import random


def findEvenNumber(numbers):
    ##################################################
    # Make your code
    ##################################################
    return


numbers = [random.randint(0, 100) for i in range(10)]
print('Original list', numbers)
gen = findEvenNumber(numbers)

for i in gen:
    print(i, end=' ')
