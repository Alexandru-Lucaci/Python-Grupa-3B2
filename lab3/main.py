

def ex1( a,b):

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

def recursivityEx3(item):
    final=[]
    if type(item) is dict:
        for key in item:
            final+=recursivityEx3(item[key])
    else:
        for i in item:
            final+= recursivityEx3(i)
    return final

def ex3(dictionar1, dictionar2):
    return list(set(recursivityEx3(dictionar1)) ^ set(recursivityEx3(dictionar2)))


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

def ex7(*sets):
    # listUnion = []
    dictionary = {}
    opList =["|","&","-"]
    firstSet = sets[0]
    for index1,set1 in enumerate(sets):
        firstSet = sets[index1]
        for index,set in enumerate (sets):
            if index != index1:
                for i in range(0,len(opList)):
                    text = str(firstSet) + str(opList[i]) + str(set)
                    print(text);
                    (aUnionB, aIntersectionB, aDifferenceB, bDifferenceA)= ex1(firstSet, set)
                    if i == 0:
                        dictionary[text] = aUnionB
                    elif i == 1:
                        dictionary[text] = aIntersectionB
                    elif i == 2:
                        dictionary[text] = aDifferenceB
                        # text = str(set) + str(opList[i]) + str(firstSet)
                        # dictionary[text] = bDifferenceA
                        # print(text)

    # firstSet=sets[index]
    return dictionary
def ex8(dictionary):
    currentKey="start"
    list=[]
    while(True):
        if(currentKey==dictionary[currentKey]):
            return list

        list+=dictionary[currentKey]

        currentKey = dictionary[currentKey]
        if list.count(currentKey) >1:
            return list




def ex9(*elements, **parameters):
    count = 0
    set_elements = set(elements)
    # print(set_elements)
    # print(parameters.count(set_elements))
    # print(parameters.items())
    for key in parameters:
        if parameters[key] in set_elements:
            count += 1
    return count
    # echivalent cred cu asta
    return len([el for el in elements if el in parameters.values()])


if __name__ == '__main__':
    exercitiu = 0
    while exercitiu != -99:
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu == 1:
            a = {2, 4, 6, 8, 9, 10, 11}
            b = {1, 2, 3, 4, 5, 7, 9, 10, 11}
            ex1(a,b)
        elif exercitiu == 2:
            string = input("Introduceti un string")
            ex2(string)
        elif exercitiu == 3:
            dict1={1:2,3:4,5:6}
            dict2={1:2,3:4,5:6}
            ex3(dict1,dict2)
        elif exercitiu == 4:
            print(ex4("a", "saluuut", href="http://python.org", _class="my-link", id="someid"))
        elif exercitiu == 5:
            ex5()
        elif exercitiu == 6:
            (a,b) = ex6([1,2,3,4,5,6,5,5,6,2])
            print("Elemente unice=",a,"Elemente duplicte=",b)
        elif exercitiu == 7:
            print(ex7({1,2},{3,4},{5,6}))
        elif exercitiu == 8:
            print(ex8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

        elif exercitiu == 9:
            print(ex9(1,2,3,4,x=1,y=2,z=3,w=5))

        else:
            break
