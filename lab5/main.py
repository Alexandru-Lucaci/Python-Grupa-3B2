import utils

sumOfNums = lambda *y, **x: sum(x.values())


def functieAdunare(*args, **kwargs):
    return sum(kwargs.values())


def ex2(*y, **x):
    print(sumOfNums(*y, **x))
    print(functieAdunare(*y, **x))

def ex3(_list):
#     return a list with all the chars in the string
    finalList =[]
    vowels = ['a','e','i','o','u']
    for i in range (0,(len(_list))):
        if _list[i] in vowels:
            finalList.append(_list[i])
    return finalList

def ex3Filter(string):
    vocale = ['a','e','i','o','u']
    return list(filter(lambda element: element in vocale, string))

ex3ListLambda = lambda string: [element for element in string if element in ['a','e','i','o','u']]
if __name__ == '__main__':
    inputul = int(input(" element : "))
    while (inputul != 0):
        if inputul == 2:
            ex2(a=1, b=2, c=3, d=4, e=5)
        elif inputul == 3:
            print(ex3("salut ce faci"))
            print(ex3Filter("salut ce faci"))
            print(ex3ListLambda("salut ce faci"))
        inputul = int(input(" element : "))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
