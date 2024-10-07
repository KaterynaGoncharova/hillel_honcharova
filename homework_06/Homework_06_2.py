from tkinter.tix import HList
while True:
    word = input('Введіть слово з літерою "h": ')
    if 'h' in word.lower():
        print(f'Слово має літеру "h" ')
        break
    else:
        print('Ви ввесли слово без літери "h" ')
