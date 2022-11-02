import os
import sys

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

    FileObject = open(fisier, "w")

    for (root, directories, files) in os.walk(director):
        for file in files:
            if file.startswith('A') or file.startswith('a'):
                print(os.path.join(root, file))
                FileObject.write(os.path.join(root, file) + "\n")

    FileObject.close()
        # for directories in files:
        #     if directories.startswith('A') or directories.startswith('a'):
        #         print(os.path.join(root, directories))
def ex2DoarDirector(director, fisier):

        FileObject = open(fisier, "w")

        files = os.listdir(director)
        for file in files:
            if os.path.isfile(os.path.join(director, file)):
                if file.startswith('A') or file.startswith('a'):
                    print(os.path.join(director, file))
                    FileObject.write(os.path.join(director, file) + "\n")
        FileObject.close()
# TODO 3)	Să se scrie o funcție ce primește ca parametru un string my_path.
# TODO Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
def ex3(my_path):
    if os.path.isfile(my_path):

        content = open(my_path, "r").read()
        if len(content) > 20:
            return content[-20:]
        else:
            raise Exception("File is too small")
    elif os.path.isdir(my_path):
        dictionary = {}
        for (root, directories, files) in os.walk(my_path):
            for file in files:
                if dictionary.get(os.path.splitext(file)[1]) is None:
                    dictionary[os.path.splitext(file)[1]] = 1
                else:
                    dictionary[os.path.splitext(file)[1]] += 1

        dictionary = sorted(dictionary.items(), key=lambda x: x[1])
        return dictionary
    # print("ex")
#     todo 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
#     todo Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.
def ex4():
    if len(sys.argv) < 1:
        raise Exception("Not enough arguments")
    final_list = []
    for el in sys.argv:
        if(el!= sys.argv[0]):
            if os.path.splitext(el)[1] != "":
                final_list.append(el)
    return final_list
def ex5(target, to_search):
    boolean = False
    if os.path.isfile(target):
        content = open(target, "r").read()
        if to_search in content:
            boolean = True
    elif os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for file in files:
                if to_search in open(target, "r").read():
                    boolean= True
    if boolean:
        return True
    else:
        raise Exception("ValueError")

def ex6(target, to_search, call_back_function):
    boolean = False
    if not os.path.exists(target):
        call_back_function(Exception("Path does not exist"))
    if os.path.isfile(target):
        content = open(target, "r").read()
        if to_search in content:
            boolean = True
    elif os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for file in files:
                if to_search in open(target, "r").read():
                    boolean = True
    if boolean:
        return True
    else:
        call_back_function(Exception("ValueError"))

def callBackFunction(exception):
    if ( type(exception) == Exception):
        print("Exception: " + str(exception))
    else:
        raise Exception("I didn't get an exception")

def ex7(path_String):
    dict = {}
    if os.path.exists(path_String):
        if(not os.path.isfile(path_String)):
            raise Exception("Path is not a file")
        dict["absolute_path"] = os.path.abspath(path_String)
        dict["file_size"] = os.path.getsize(path_String)
        dict["file_extension"] = os.path.splitext(path_String)[1]
        dict["can_read"] = os.access(path_String, os.R_OK)
        dict["can_write"] = os.access(path_String, os.W_OK)
        return dict
    else:
        raise  Exception("Path does not exist")
    print("ex")
def ex8(dir_path):
    list_of_files = []
    files = os.listdir(dir_path)
    for file in files:
        if os.path.isfile(os.path.join(dir_path, file)):
            print(os.path.join(dir_path, file))
            list_of_files.append(os.path.abspath(os.path.join(dir_path, file)))
    return list_of_files
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
            ex2("D:\Microsoft",'D:\Python-Grupa-3B2\lab4\Files\ex2.txt')
            ex2DoarDirector("D:\\Ubuntu",'D:\Python-Grupa-3B2\lab4\Files\ex2.txt')
        elif exercitiu == 3:
            print(ex3("D:\Python-Grupa-3B2\lab4"))

        elif exercitiu == 4:
            # print(sys.argv[1])
            print(ex4())
        elif exercitiu == 5:
            print(ex5("D:\Python-Grupa-3B2\lab4\Files\ex2.txt", "a"))
        elif exercitiu == 6:
            print(ex6("D:\Python-Grupa-3B2\lab4\Files\ex2.txt", "asss", callBackFunction))
        elif exercitiu == 7:
            print(ex7("D:\Python-Grupa-3B2\lab4\Files\ex2.txt"))
        elif exercitiu == 8:
            print(ex8("D:\Python-Grupa-3B2\lab4\Files"))
        elif exercitiu == 9:
            ex9()
        elif exercitiu == 10:
            ex10()
        else:
            break

