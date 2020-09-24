import re
import csv

inp = 'target.txt'


def get_reader(inp):
    with open(inp, 'r', encoding='utf8') as file:
        text = file.read(20000)  # указываем размер считывания из файла
        pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+')  # создали шаблон
        result = pattern.findall(text)
        lister = []
        s = 0
        for i in result:
            lister.append(i)
            s += 1
    print("Количество строк = ", s)
    return lister


def get_writer(lister):
    with open('output.txt', 'a') as file:
        for index in lister:
            file.write(index + '\n')


def main():
    get_writer(get_reader(inp))


if __name__ == '__main__':
    main()
