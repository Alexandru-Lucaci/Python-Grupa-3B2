# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# CUrse 1
def findType(n):
    return type(n)
n=True
print(findType(n))
if(findType(n)==bool):
    print("it is a boolean")

def formatingString(name, value):
    return "The value of {} is {}".format(name, value)
    return "The value of %(name) is %(value)" % {"name": name, "value": value}
    return f"The value of {name} is {value}"

print(formatingString("a", 1))



def stringTypes():
    s="Python"+" "+"is"+" "+"awesome"+"Python"+" "+"is"+" "+"awesome"
    print(s)
    s="A"+"12"*3
    print(s)
    print("A" in "ABC")
    print("A" not in "ABC")
    s="Python"+"Exam"
    print(s[1:7:2])
    s.startswith("Py")
    s.endswith("am")
    s="Python "+"Exam "+"Python "+"Exam "+"Python "+"Exam "+"is "+"awesome"
    print(s.replace("Python", "Java", 2))
    print(s.find("Exam"))
    print(s.index("Exam"))
    print(s.rindex("Exam"))
    print(s.count("Exam"))
    print(s.upper())
    print(s.lower())
    print(s.title())
    print(s.capitalize())
    print(s.swapcase())
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    print(s.split(" "))
    s="Python Exam Python Exam Python Exam is awesome"
    print(s)
    print(s.isalpha())
    print(s.isalnum())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())
# stringTypes()


def buitInFunctionString():
    s="Python Exam Python Exam Python Exam is awesome"
    print(hex(123))
    format(123, "b")

buitInFunctionString()
#  Lambda functions -> functions without any name
def lamdaFunctions():
    addition = lambda x, y: x + y
    print(addition(2, 3))

def ComputeSumAndProduct(*list):
    sum=0
    product=1
    for i in list:
        sum+=i
        product*=i
    return (sum, product)
# is prime function using lambda
def isPrime(n):
    return all(n%i!=0 for i in range(2, n))

def ListAndFunctional():
    x= [i for i in range (1, 11)]
    print(x)
    y= [i for i in range (1, 11) if i%2==0]
    print(y)
    z= [i*i for i in range (1, 11)]
    print(z)
    x=[[x,y] for x in range(1,10) for y in range(1,10) if (x+y)%2==0 ]
    print(x)
    x=[i for i in range(1,9999) if isPrime(i)]
    print(x)
    x=[x for x in range(1,9999) if len([y for y in range(2,x//2+1) if x%y==0])==0]
    print(x)
# ListAndFunctional()

def listFunction():
    x=[1,2,3,4,5,6,7,8,9,10]
    x.append(4)
    x+=["a", "b", "c"]
    x.extend((1,2,3))
    print(x)
    x=[1,2,3]
    x.insert(1,"a")
    x.insert(-1,"b")
    x.insert(len(x),"c")

    # remove -> remove the first occurence of the element
    x.remove(1)
    # pop -> remove the last element
    x.pop()
    # del -> remove the element at the given index
    del x[0]
    # clear -> remove all the elements
    x.clear()
    # index -> return the index of the first occurence of the element
    x=[1,2,3,4,5,6,7,8,9,10]
    # x.index(1)
    # count -> return the number of occurences of the element
    # x.count(1)
    # y= list(x)
    y=x.copy()
    y=x[:]
    # y= x.index(1)
    y= 1 in x
    x.sort(reverse=True)
    print(x)
    x.sort(key=lambda x: x%2==0)
    print(x)

# listFunction()

def mapAndFilter():
    x=[1,2,3,4,5,6,7,8,9,10]
    y=map(lambda x: x*x, x)
    print(list(y))
    y=filter(lambda x: x%2==0, x)
    print(list(y))
    z=list(map(lambda e1,e2: e1+e2, x,y))

    x=[1,2,3,4,5,6,7,8,9,10]
    y = list(filter(lambda x: x%2==0, x))

    print(list(map(lambda x: x*2, range(1,19))))
    print(list(filter(lambda x: x%7==1,range(1,100))))
    x=[2,1,4,3,5]
    y=sorted(x)

# mapAndFilter()

def allAndAny():
    x=[2,1,3,4,5]
    y=all(i>0 for i in x)
    y=any(i>0 for i in x)
def zipAndUnzip():
    x=[1,2,3,4,5]
    y=[6,7,8,9,10]
    z=zip(x,y)
    print(list(z))
    x,y=zip(*z)
    print(x)
    print(y)
# if __name__ == '__main__':
#     print('Hello')

def tryFunctions():
    try:
        x=1/0
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:
        print("Error")
    else:
        print("No error")
    finally:
        print("Finally")

def tryFunctionsElse():
    try:
        x=1/1
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:
        print("Error")
    else:
        print("No error")
    finally:
        print("Finally")
tryFunctions()
tryFunctionsElse()
# exceptia generica trebuie sa fie ultima exceptie
def tryFunctionsFinally():
    try:
        x=1/0
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:
        print("Error")
    else:
        print("No error")
    finally:
        print("Finally")

# else -> se executa daca nu a aparut nicio exceptie
# finally -> se executa indiferent daca a aparut o exceptie sau nu
# finally trebuie sa fie totimpul ultimul bloc de cod

tryFunctionsFinally()

def tryFunctionsMultipleExceptions():
    try:
        x=1/0
    except (ZeroDivisionError, TypeError):
        # tratez cu acest bloc si exceptia ZeroDivisionError si exceptia TypeError
        print("ZeroDivisionError")
    except:
        print("Error")
    else:
        print("No error")
    finally:
        print("Finally")

# tryFunctionsMultipleExceptions()

def tryFunctionsAs():
    try:
        x=5/0
    except Exception as e:
        print(str(e))
# incorporeaza info despre acea exceptie


def tryFunctionsAsMultipleExceptions():
    try:
        x=5/0
    except (ZeroDivisionError, TypeError) as e:
        print(str(e), type(e))

# tryFunctionsAsMultipleExceptions()

#  raise exception
def tryFunctionsRaise():
    try:
        raise Exception("Error, testing raise command")
    except Exception as e:
        print(str(e))
tryFunctionsRaise()

def tryFunctionsRaiseWithParam():
    try:
        raise Exception("Param1",10,"Param3")
    except Exception as e:
        params = e.args
        print(len(params))
        print(params[0])

tryFunctionsRaiseWithParam()

try:
    try:
        x=5/0
    except Exception as e:
        print(str(e))
        raise
except Exception as e:
    print("return from raise ->", e)


# uneori vrei sa creezi un nou tip de exceptie dar vrei sa o legi cu alta exceptie

def exceptionInlantuite():
    try:
        x=5/0
    except Exception as e:
        raise Exception("Error in exceptionInlantuite") from e
# utila cand o exceptie o transformam in alta exceptie si sa putem sa o inlantuim

# exceptionInlantuite()

# ASSERT - verifica daca o conditie este adevarata, daca e corecta valida trece mai departe dar daca nu e valida arunca o exceptie
# assert <conditie>, <mesaj>
def assertFunction():
    try:
        x=1
        assert x==1, "x nu este egal cu 1"
        assert x==2, "x nu este egal cu 2"
    except Exception as e:
        print(e)
assertFunction()


# PASS - nu face nimic, este folosit cand nu vrei sa faci nimic in blocul de cod
# pass este neindicat sa fie folosit in blocul de cod
# try:
#     x=10/0
# except:
#     pass


# raise SystemExit -> arunca exceptia SystemExit
# raise SystemExit trebuie sa opresc imediat executia programului
# daca vreau sa ies brusc, fara sa mai fac nimic, folosesc raise SystemExit


#  Modulele sunt fisiere cu extensia .py, sunt librariile din python care extind
# functionalitatea limbajului python
#  de multe ori modulele nu sunt scrise in python ci in alte limbaje de programare
#  cum ar fi c, c++, java, etc

#  pentru a folosi un modul trebuie sa il importam
#  import <nume_modul>
#  import <nume_modul> as <alias>
#  from <nume_modul> import <nume_functie>
#  from <nume_modul> import <nume_functie> as <alias>
# from <nume_modul> import *
#  import <nume_modul>,<nume_modul2>,<nume_modul3>,<nume_modul4>...

def modules():
    import math
    print(dir(math))
# dir() -> returneaza o lista cu toate functiile dintr-un modul
# Module:
#  math
#  collections
#  ctypes - a lucra cu biblioteci din alte limbaje de programare, a lucra cu structuri de date cu lungime fixa
# datetime
#  random
#  email
#  json
#  os - > ce tine de functii os-ul
#  re - > regular expressions
#  socket - > comunicare cu alte programe, tot ce tine de networking
#  sys - > ce tine de sistemul de operare, tot ce tine de input output
#  threading - > multithreading
#  subprocess - > a lucra cu procese
#  urllib - > a lucra cu url-uri
#  xml - > a lucra cu xml
    # Modulul sys
    #  sys.argv -> returneaza o lista cu parametrii din linia de comanda
    #  sys.platform -> returneaza platforma pe care ruleaza programul
    #  sys.stdin -> returneaza un obiect de tip file care reprezinta intrarea standard
    #  sys.stdout -> returneaza un obiect de tip file care reprezinta iesirea standard
    #  sys.stderr -> returneaza un obiect de tip file care reprezinta iesirea standard pentru erori
    #  sys.path -> returneaza o lista cu toate directoarele din care se pot importa modulele
    #  sys.modules -> returneaza un dictionar cu toate modulele importate, incarcate deja in memorie
    #  sys.exit() -> iesire din program

    import sys
    print("first parameter is ", sys.argv[0]) # mereu este numele scriptului
#   suma tuturor parametrilor dati la linia de comanda

    suma = 0
    try:
        for val in sys.argv[1:]:
            suma += int(val)
        print("suma este ", suma)
    except ValueError:
        print("Parametrii trebuie sa fie numere")
    else:
        print("No error")

#     Modulul OS
#  os.getcwd() -> returneaza directorul curent
#  os.listdir(".") -> returneaza o lista cu fisierele din directorul curent
#  os.chdir(<path>) -> schimba directorul curent
#  os.listdir(<path>) -> returneaza o lista cu toate fisierele dintr-un director
#  os.mkdir(<path>) -> creaza un director
#  os.rmdir(<path>) -> sterge un director
#  os.remove(<path>) -> sterge un fisier
#  os.path.exists(<path>) -> verifica daca un fisier sau director exista
#  os.path.isfile(<path>) -> verifica daca un fisier exista
#  os.path.isdir(<path>) -> verifica daca un director exista
#  os.path.getsize(<path>) -> returneaza marimea unui fisier
#  os.path.abspath(<path>) -> returneaza calea absoluta a unui fisier
#  os.path.split(<path>) -> returneaza o pereche (director, fisier) dintr-o cale
#  os.path.splitext(<path>) -> returneaza o pereche (nume_fisier, extensie) dintr-o cale
#  os.path.join(<path1>, <path2>, <path3>, ...) -> returneaza o cale concatenata din toate argumentele
# os.path.basename(<path>) -> returneaza numele fisierului dintr-o cale
# os.path.dirname(<path>) -> returneaza numele directorului dintr-o cale
# os.path.commonprefix(<path1>, <path2>, <path3>, ...) -> returneaza prefixul comun din toate argumentele
# os.path.commonpath(<path1>, <path2>, <path3>, ...) -> returneaza calea comuna din toate argumentele
# os.path.normpath(<path>) -> returneaza o cale normalizata
# os.path.normcase(<path>) -> returneaza o cale cu litere mici
#
    import os
    print(os.path.join("C:","Windows","System32","drivers","etc","hosts"))
    print(os.path.dirname("C:WindowsSystem32driversetchosts")) #returneaza numele folderului
    print(os.path.splitext("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza extensia
    print(os.path.basename("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza numele fisierului
    print(os.path.isdir("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza daca este director
    print(os.path.isfile("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza daca este fisier
    print(os.path.exists("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza daca exista
    # print(os.path.getsize("C:\\Windows\\System32\\drivers\\etc\\hosts.txt")) #returneaza marimea

#     Listing the contents of a folder recursively
    import os
    def listdir(path):
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                listdir(os.path.join(path, file))
            else:
                print(os.path.join(path, file))

    # listdir("C:\\Windows\\System32")

    for(root, directories, files) in os.walk("."):
        for file in files:
            print(os.path.join(root, file))

    os.system("dir *.* /a") #executa comanda dir in cmd

modules()