import re



pag = open('textov.txt').read() #создали переменную pag и передали ей содержимое файла методом read
result = re.findall(r':\w{30}' , pag) #с помощью регулярного выражения нашли в тексте слова с : и 30 символьные

print(result)
#print(result)

#itog = open('resultat.txt', 'w') #создали файл с медодом записи
#itog.write(str(result))          # передали переменной и записали данные преобразовав в тип string


with open("resultat.txt", "w") as file: # открыли файл 
    for  line in result:                 # создали цикл построчно в списке result
        file.write(line + '\n')          # записали в файл построчно с помощью перехода на новую строку



#itog.close() # закрыли файл
print('Готово!  ')



