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
stringTypes()


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
ListAndFunctional()

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

listFunction()

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

mapAndFilter()

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