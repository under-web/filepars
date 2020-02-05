import re
import os


pag = open('textov.txt').read() #создали переменную pag и передали ей содержимое файла методом read
result = re.findall(r'.' , pag) #с помощью регулярного выражения нашли в тексте нужную иформацию функцией findall

#print(result)

itog = open('resultat.txt', 'w') #создали файл с медодом записи
itog.write(str(result))          # передали переменной и записали данные преобразовав в тип string










itog.close() # закрыли файл
print('Готово!  ')

