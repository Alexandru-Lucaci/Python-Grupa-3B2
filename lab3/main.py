

def ex1():
    a={2,4,6,8,9,10,11}
    b={1,2,3,4,5,7,9,10,11}
    aUnionB = a.union(b)
    aIntersectionB = a.intersection(b)
    aDifferenceB = a.difference(b)
    bDifferenceA = b.difference(a)
    return (aUnionB, aIntersectionB, aDifferenceB, bDifferenceA)

def ex2(stringwithProp):
    letterDictionary = {}
    stringwithProp = stringwithProp.lower()
    for letter in stringwithProp:
        if letter != ' ':
            if letter in letterDictionary:
                letterDictionary[letter] += 1
            else:
                letterDictionary[letter] = 1

    print(letterDictionary)
def ex3(dictionar1, dictionar2):
    dictionar1 = dictionar1.copy()
    dictionar2 = dictionar2.copy()
    for key in dictionar1:
        if key in dictionar2:
            if dictionar1[key] == dictionar2[key]:
                dictionar1.pop(key)
                dictionar2.pop(key)
    if len(dictionar1) == 0 and len(dictionar2) == 0:
        return True
     # return len(dictionar1) == len(dictionar2) and all([dictionar1[key] == dictionar2[key] for key in dictionar1])
    return False

a=(1,1)
dictionar = {1:22}
print(dictionar)


def ex4(tag, content, **parameters):
    tagCreation = "<" + tag
    for key, value in parameters.items():
        tagCreation += " " + key + "=\"" + value + "\""
    tagCreation += ">" + content + "</" + tag + ">"
    return tagCreation

def ex5():
    print("ex")
#     idk yet
def ex6(listA):
    setA = set(listA)
    # setB = set(listB)
    a =len(setA)
    b = len(listA)-a
    return (a,b)

def ex7():
    print("ex")
def ex8():
    print("ex")
def ex9():
    print("ex")
def ex10():
    print("ex")


if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            ex1()
        elif exercitiu == 2:
            string = input("Introduceti un string")
            ex2(string)
        elif exercitiu == 3:
            ex3()
        elif exercitiu == 4:
            print(ex4("a", "saluuut", href="http://python.org", _class="my-link", id="someid"))
        elif exercitiu == 5:
            ex5()
        elif exercitiu == 6:
            (a,b) = ex6([1,2,3,4,5,6,5,5,6,2])
            print("Elemente unice=",a,"Elemente duplicte=",b)
        elif exercitiu == 7:
            ex7()
        elif exercitiu == 8:
            ex8()
        elif exercitiu == 9:
            ex9()
        elif exercitiu == 10:
            ex10()
        else:
            break
