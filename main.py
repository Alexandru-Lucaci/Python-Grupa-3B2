# This is a sample Python script.
import string


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def cmmdc(a,b):
    if(a==b):
        return a;
    else:
        if(a>b):
            return cmmdc(a-b,b)
        else:
            return cmmdc(a,b-a)


def ex1():
    n = int(input("Nr. de elemente>>"))
    # print(cmmdc(15,80))
    a = int(input('Introdu un numar>>'))
    while(n!=1):
        b= int(input('Introdu un numar>>'))
        celMaiMareDivizor = cmmdc(a,b)
        a=b
        n=n-1
    print("Cel mai mare divizor este %d"%celMaiMareDivizor)
def ex2():
    string = input("Introdu sirul> ")
    vocale = "aeiou"
    nr = 0
    string = string.lower()
    for index in vocale:
        nr+=string.count(index)

    print("In total sunt %d vocale"%nr)

def ex3():
    firstString = input("Introdu primul cuv >")
    secondString = input("Introdu propozitia")

    firstString.lower()
    secondString.lower()
    print("Cuvantul %s apare in textul '%s' de %d ori"%(firstString,secondString,secondString.count(firstString)))

def ex4():
    string = input('Introdu textul> ')
    for car in string:
        if(car >= 'A' and car <='Z'):
            # print("yes")
            string = string.replace(car,"_"+car.lower())

    if(string.startswith("_")):
        # print('Yess')
        string= string.replace('_','',1)
    print(string)
def ex5():
    a = ["firs", "n_lt", "oba_", "htyp"]
    a= ["12","56"]
    m = len(a)
    n = len(a[0])
    k = 0
    l = 0

    while (k < m and l < n):
        for i in range(l, n):
            print(a[k][i])
        k += 1
        for i in range(k, m):
            print(a[i][n - 1])
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i])
            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l])

            l += 1

def ex6():
    number = int(input('n='))
    copie = number
    newNum = 0
    while copie:
        newNum=newNum*10+copie%10
        copie//=10

    print("%d si %d"%(number,newNum))
    if number==newNum:
        print('da')
    else:
        print('nu')

def ex7():
    sir = input('Sirul>> ')

    contor = 1
    number =''
    for index in sir:
        if(index >= '0' and index <='9'):
            number = number + index
            contor = 2
        elif contor == 2:
            break
    if number != '':
        number = int(number)
        print(number)
    else:
        print('Nu am gasit niciun numar, scuze')
def ex8():
    number = int(input('Introdu un numar'))
    number = format(number,'b')
    # count = number.count("1")
    print("Numarul de 1 este %d"%(number.count('1')))
# Press the green button in the gutter to run the script.
def ex9():
    print(list(string.ascii_letters))
    sir = input('Sir>> ')
    maxx=0
    lit=''
    for litera in list(string.ascii_letters):
        if sir.count(litera)>maxx:
            maxx=sir.count(litera)
            lit=litera
    print("Litera '%s' apare de %d ori"%(lit,maxx))
def ex10():
    sir = input('Sir>> ')
    print("Sunt %d cuvinte"%(sir.count(' ')+1))

if __name__ == '__main__':
    # print_hi('PyCharm')
    # ex1();
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex8()
    # ex7()
    # ex9()
    ex10()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
