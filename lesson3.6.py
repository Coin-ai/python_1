# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def up_tit(word):
    # title?
    abc='abcdefghijklmnopqrstuvwxyz '
    ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    if (set(word)-set(abc)):
        print('only lowercase letters a-z')
        return False
    if word:
        ind=abc.index(word[0])
        word=ABC[ind]+word[1:]
    else:
        word=' '
    return word

def main():
    str=input('enter text: ')
    words=str.split(' ')
    print(words)
    for ind,val in enumerate(words):
        if w:=up_tit(val):
            words[ind]=up_tit(val)
        else:
            words=False
            break
    if words:
        print(' '.join(words))
    else:
        main()

main()