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


if __name__ == '__main__':
    # print_hi('PyCharm')
    exercitiu = 0
    while exercitiu!=-99 :
        exercitiu = int(input("Alege un exercitiu"))

        if exercitiu==1:
            number = int(input("numar >"))
            print(fib(10))
        elif exercitiu==2:
            print("finish")
        else:
            print("done")


