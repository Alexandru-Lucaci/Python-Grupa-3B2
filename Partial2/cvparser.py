

def f():
    import sys
    # for i in sys.argv[1:]:
    #     print(i)
    import os
    if len(sys.argv) < 1 :
        raise Exception('[ERROR] nr paramatrii insuficiente')

    fisier = sys.argv[1]
    finalList = []
    finalDict = {}
    if(os.path.exists(fisier)):
        try:
            f = open(fisier, 'r')
        except Exception:
            raise Exception('[ERROR] - IO error')
        index = 0
        for line in f:
            if index == 0:
                # am luat prima linie
                linia1= line.split(',')
                linia2 =[]
                for i in linia1:
                    # remove the \n from the end of the string
                    linia2.append(i.replace('\n',''))
                linia1= linia2


                for ind,i in enumerate(linia1):

                    if sys.argv[2] in i:
                        if(i.count(sys.argv[2])>1):
                            raise Exception('[ERROR] - invalid format - duplicate columns')
                        index =int(ind+1)
                        # print(ind+1)\
                if(index == 0):
                    raise Exception('[Error]- unknown column name')
            else:

                # print(index)
                if(index > 0):
                    # print('OK')
                    # print(line)
                    i = line.split(',')

                    # remove the '\n' from the final element
                    i[-1] = i[-1].replace('\n','')
                    if(len(i) != len(linia1)):
                        raise Exception('[ERROR] - invalid format -  different words on line ' + str(index))
                    if  i[index - 1].lower()  == sys.argv[2].lower():
                        # print('[OK]')
                        finalList[0] = '[OK]'
                    else:
                        id = i[index - 1].lower()
                        # print("ID este" + id)

                        if id in finalDict.keys():
                            finalDict[i[index - 1].lower()] += 1
                        else:
                            finalDict[i[index - 1].lower()] =  1

        # print(finalDict)
        finalList = sorted(finalDict, key=finalDict.get, reverse=True)


        print('[OK]')
        for i in finalList:
            print(i)

    else:
        raise Exception("[ERROR] - file not found ")

try:
    f()
except Exception as e:
    print(e)