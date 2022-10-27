import os


def print_hi(name):
    print(f'Hi, {name}')
def ex1nefolder(directory):
    # get al the extension of the files in the directory
    files = os.listdir(directory)
    extensions = []
    for file in files:
        directoryMade = os.path.join(directory, file)
        # print(directoryMade)
        extensions.append(os.path.splitext(file)[1])
    extensions = set(extensions)
    extensions = sorted(extensions)
    return extensions
def ex1(directory):

#     get al the extension of the files in the directory
    files = os.listdir(directory)
    extensions = []
    for file in files:
        directoryMade = os.path.join(directory, file)
        # print(directoryMade)
        if os.path.isdir(directoryMade):
            # print("Is dir " + file)
            extensions.extend(ex1(directoryMade))
        else:

            # print("File "+file)
            extensions.append(os.path.splitext(file)[1])
    extensions = set(extensions)
    extensions = sorted(extensions)

    return extensions


# TODO: Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
def ex2(director, fisier):
    
    for (root, directories, files) in os.walk(director):
        for file in files:
            if file.startswith('A') or file.startswith('a'):
                print(os.path.join(root, file))

        # for directories in files:
        #     if directories.startswith('A') or directories.startswith('a'):
        #         print(os.path.join(root, directories))
def ex3():
    print("ex")
def ex4():
    print("ex")
def ex5():
    print("ex")
def ex6():
    print("ex")
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
            print(ex1("D:\Python-Grupa-3B2"))
            print(ex1nefolder("D:\Python-Grupa-3B2"))
        elif exercitiu == 2:
            ex2("D:\Microsoft",'')
        elif exercitiu == 3:
            ex3()
        elif exercitiu == 4:
            ex4()
        elif exercitiu == 5:
            ex5()
        elif exercitiu == 6:
            ex6()
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

