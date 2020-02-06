import re



pag = open('thread-f12590f508.html').read() #создали переменную pag и передали ей содержимое файла методом read
result = set(re.findall(r':\w{10,40}' , pag)) #с помощью регулярного выражения нашли в тексте слова с 10 : и 30 символьные уникально

print(result)
#print(result)

#itog = open('resultat.txt', 'w') #создали файл с медодом записи
#itog.write(str(result))          # передали переменной и записали данные преобразовав в тип string


with open("resultat.txt", "w") as file: # открыли файл 
    for  line in result:                 # создали цикл построчно в списке result
        file.write('magnet:?xt=urn:btih' + line + '\n')          # записали в файл построчно с помощью перехода на новую строку

print(len(result)) 

#itog.close() # закрыли файл
print('Готово!  ')




