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
    s="Python"+" "+"is"+" "+"awesome"
    print(s)
    s="A"+"12"*3
    print(s)
    print("A" in "ABC")
    print("A" not in "ABC")
    s="Python"+"Exam"
    print(s[1:7:2])


if __name__ == '__main__':
    print('Hello')