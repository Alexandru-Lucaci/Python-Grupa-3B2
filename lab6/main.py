# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def ex1(string_words):
    list_words = string_words.split(' ')
    while('' in list_words):
        try:
            list_words.remove('')
        except ValueError:
            pass

    return list_words

def ex2(regex_string,text_string,x):
    # and returns those long-length x substrings that match the regular expression
    import re
    list_words = []
    for match in re.finditer(regex_string, text_string):
        if len(match.group()) == x:
            list_words.append(match.group())
    return list_words

print(ex2(r'\d+', 'abc123def456ghi789', 3))

# Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns a list of strings that match on at least one regular expression given as a parameter.
def ex3(string_words, list_regex):
    import re
    list_words = []
    for regex in list_regex:
        list_words.extend(re.findall(regex, string_words))
    return list_words
# Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags whose attributes are class="url" si name="url-form" si data-id="item".
def ex4(path_xml, attrs):
    import sys
    import os
    import re
    if not os.path.exists(path_xml):
        print("File not found")
        sys.exit()
    f = open(path_xml, "r")
    lines = f.readlines()
    f.close()
    finded_list = []
    for index,line in enumerate(lines):
        match = True
        for att in attrs:
            # print('avem cu ' + att + ' ' + attrs[att])
            if  not re.match(r'(.*)'+att+'="'+attrs[att]+'"(.*)', line):
                match = False
        if match:
            separator = re.search(r'<(.*)\s(.*)>', line)
            separator = separator.group(1)
            # print(separator)
            # print(line)
            finded_list.append(line)
            if not re.match(r'(.*)</'+separator, lines[index]):
                index+=1
                while not re.match(r'(.*)</'+separator, lines[index]):
                    # print(lines[index])
                    finded_list.append(lines[index])
                    index+=1
                else:
                    # print(lines[index])
                    finded_list.append(lines[index])

    return finded_list


def ex5(path_xml, attrs):
    retrn_list = []
    # dict={}
    for i in attrs:
        dict={}
        dict[i] = attrs[i]
        lista= ex4(path_xml, dict)
        if len(lista)>0:
            retrn_list.extend(lista)
    return retrn_list
exx= ex5("D:\\git\\GitHub\PythonUdemy\\text.html", {'class': 'ccfdf', 'name': 'url-form', 'data-id': 'item'})
for i in exx:
    print(i)


def ex6(text_param):
    import re
    list_words = ''
    text_param = text_param.split(' ')

    for word in text_param:
        # word finished with a letter
        punctuation = ''
        if not re.match(r'(.*)\w$', word):
            # daca am cumva un semn de punctuatie la final
            punctuation = word[-1]
            word = word[:-1]
        # verific daca am cumva
        if re.match(r'[aeiouAEIOU]+\w*[aeiouAEIOU]$', word):
            new_word ='';
            for index,i in enumerate(word):
                if (index+1)%2==1:
                    new_word+='*'
                else:
                    new_word+=word[index]
            word = new_word
        list_words+=word+punctuation
        list_words+=' '
    return list_words

print(ex4("D:\\git\\GitHub\PythonUdemy\\text.html", {"class": "ccfdf"}))
text = "Lorem Ipsum is simply dummy ana text are mere of the printing and andreea analiza apa, typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(ex6(text))

def ex7(string_text):
    import re
    if re.match(r'(.*)\D+(.*)',string_text):
        raise Exception('Nu este numar')
    else:
        if len(string_text) == 13:
            # print('here')
            if re.match(r'[12]|[56]\d{12}',string_text):
                # print('match')
                if int(string_text[3:5])>12:
                    raise Exception('Luna invalida')
                elif int(string_text[5:7])>31:
                    raise Exception('Zi invalida')
                return True
            else:
                raise Exception('Cod invalid')
        raise Exception('Numai mai mic decat 13 cifre')

def ex8(directory, regular_expressions):
    import os
    import re
    if not os.path.exists(directory):
        raise Exception('Directory not found')
    if not os.path.isdir(directory):
        raise Exception('Not a directory')

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,file)):
            boolean_just_the_name = False
            boolean_and_text = False
            for i in regular_expressions:
                if re.match(i, file) :
                    print('matched 0')
                    # print(file)
                    f = open(os.path.join(directory,file), "r")
                    text = f.read()
                    print(text)
                    f.close()
                    print(i)
                    if re.match(i, text):
                        print ('matched')
                        boolean_and_text = True
                        boolean_just_the_name = True
                        # print('>>'+file)
                    else:
                        boolean_just_the_name = True

                        # print(file)
            if boolean_and_text:
                print('>>'+file)
            else:
                if boolean_just_the_name:
                    print(file)

        # else:
            # ex8(os.path.join(directory,file),regular_expressions)
            # raise Exception(f'{file} Not a file')
ex8('D:\\javascript\\tutorial', [r'.*\.txt$', r'.*\.js$', r'.*\.html$'])
if __name__ == '__main__':
    print(ex1('Ana are 12 3     s      mere'))
    try:
        print(len('6221131234456'))
        if ex7('1311223311219'):
            print('CNP valid')
        else:
            print('CNP invalid')
    except Exception as e:
        print(e)
