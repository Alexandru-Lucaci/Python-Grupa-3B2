# import utils

sumOfNums = lambda *y, **x: sum(x.values())


def functieAdunare(*args, **kwargs):
    return sum(kwargs.values())


def ex2(*y, **x):
    print(sumOfNums(*y, **x))
    print(functieAdunare(*y, **x))


def ex3(_list):
    #     return a list with all the chars in the string
    finalList = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, (len(_list))):
        if _list[i] in vowels:
            finalList.append(_list[i])
    return finalList


def ex3Filter(string):
    vocale = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda element: element in vocale, string))


ex3ListLambda = lambda string: [element for element in string if element in ['a', 'e', 'i', 'o', 'u']]


# print(type("test"))
# if(type("test") == str):
#     print("test")

def ex4(*listItems, **dictItems):
    #    iterate listitems and return only the dictionaries
    returnList = []
    # for i in listItems:
    #     if type(i) == dict:
    #         if len(i.values()) >=2:
    #             for j in i.values():
    #                 if type(j) == str and len(j) >= 3:
    #                     returnList.append(i)
    #                     break
    for i in listItems:
        if type(i) == dict:
            if len(i.values()) >= 2:
                for j in i.keys():
                    if type(j) == str and len(j) >= 3:
                        returnList.append(i)
                        break

    for i in dictItems.values():
        if type(i) == dict:
            if len(i.values()) >= 2:
                for j in i.keys():
                    if type(j) == str and len(j) >= 3:
                        returnList.append(i)
                        break
    # print( returnList)
    print(returnList)

# print(type([1,2,3]))
def ex5(*listItems):
    returnList = []
    for i in listItems:
        if type(i) == dict:
            for j in i.values():
                if isNumber(j):
                    returnList.extend(i)
                    break
        if type(i) == list:
            returnList.extend(ex5(*i))
        if type(i) == set:
            returnList.extend(ex5(*i))
        if isNumber(i):
            returnList.append(i)
    return set(returnList)

def ex6(listNumbers):
    evenList = list(filter(lambda element: element % 2 == 0, listNumbers))
    oddList = list(filter(lambda element: element % 2 == 1, listNumbers))
    returnList = []
    for i in range(0, len(evenList)):
        returnList.append((evenList[i], oddList[i]))
    return returnList

def isNumber(x):
    try:
        if(type(x)== str):
            return False
        float(x)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


if __name__ == '__main__':
    inputul = int(input(" element : "))
    while inputul != 0:
        if inputul == 2:
            ex2(a=1, b=2, c=3, d=4, e=5)
        elif inputul == 3:
            print(ex3("salut ce faci"))
            print(ex3Filter("salut ce faci"))
            print(ex3ListLambda("salut ce faci"))
        elif inputul == 4:
            ex4({"input": 1}, {'a': 5, 'b': 7, 'aac': 'eeee'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': "1"}, 3764,
                dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})
        elif inputul == 5:
            print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
        elif inputul == 6:
            print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
        inputul = int(input(" element : "))
