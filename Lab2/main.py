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
        else:
            print("done")


