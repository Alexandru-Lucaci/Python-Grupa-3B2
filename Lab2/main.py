# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fib(number):
    if number<=0 :
        return [0]
    lista = [0,1]
    for i in range (2,number):
        lista.append(lista[len(lista)-1]+lista[len(lista)-2])
    return lista

def isPrime(number):
    if number%2==0 :
        return False
    sq = number**0.5+1
    for index in range(3,int(sq),2):
        if number%index == 0:
            return False
    return True

# print(isPrime(11))
def ex2(list):
    returnedList = []
    for i in list:
        if(isPrime(i)):
            returnedList+= i
    return returnedList
def ex3(listA, listB):
    AReunitB =[]
    AintersectatB =[]
    AminusB=[]
    BminusA =[]
    for var in listA:
        if listB.count(var) > 0:
            AintersectatB.append(var)
        AReunitB.append(var)
    for var in listB:
        if AReunitB.count(var) == 0:
            AReunitB.append(var)

    for var in listA:
        if var not in listB:
            AminusB.append(var)

    for var in listB:
        if var not in listA:
            BminusA.append(var)

    AReunitB.sort()
    AintersectatB.sort()
    AminusB.sort()
    BminusA.sort()
    return (AReunitB, AintersectatB, AminusB, BminusA)

def ex4(listSounds, listOrder, poz):

    print(listSounds[poz])
    music=[]
    for index in listOrder:
        poz+=index
        if(poz>=len(listSounds)):
            poz=poz%len(listSounds)
            music+=listSounds[poz]
            print(listSounds[poz])
        else:
            music += listSounds[poz]
            print(listSounds[poz])

    return music
def ex5(matrix):
    # 00 01 02
    # 10 11 12
    # 20 21 22
    # newMat =[]
    for i in range(0,len(matrix)):
        for j in range (0,len(matrix[0])):
            if i>j :
                matrix[i][j]=0;
    return matrix

if __name__ == '__main__':
    # print_hi('PyCharm')
    exercitiu = 0
    while exercitiu!=-99 :
        exercitiu = int(input("Alege un exercitiu"))
        if exercitiu==1:
            number = int(input("numar >"))
            print(fib(number))
        elif exercitiu==2:
            print(ex2([1,2,3,4,5,6,7,8]))
        elif exercitiu==3:
            print(ex3([2,4,5,6],[1,3,5,7]))
        elif exercitiu==4:
            ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
        elif exercitiu==5:
            a=[[1,2,3], [2,3,4],[4,5,6]]
            print(ex5(a))




