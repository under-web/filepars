import os
import re



doo = os.walk('D:\\nuznaya\\directoria') # указываем нужную директорию 

lst = [] # создаем пустой список

for root, dirs, files in doo:	#создаем цикл для выявления нужных файлов с расширением html (например)
	for f in files: 
		if f.endswith('.html'):   # если файл html то добавляем его в список
			lst.append(f)         # добавили в конец списка
			print(f)
		else:
			pass                  # если другое расширение пасуем

print(len(lst))  # выводим количество елементов списка

for h in lst: # цикл для списка 
	s = 'D:\\имя\\пути\\' + h # обьединяем путь с именами из списка для дальнейшей с ним работы (передачи в функцию в которой будет выполняться работа по поиску нужной инфы по его полному пути к файлу)
	with open('road_in_list.txt', 'a', encoding='utf8') as wr: # метод для записи в файл в режиме добавления
		wr.write(s + '\n') # запишем построчно
	


#pag = open('thread-f12590f508.html').read() #создали переменную pag и передали ей содержимое файла методом read
#result = set(re.findall(r':\w{10,40}' , pag)) #с помощью регулярного выражения нашли в тексте слова с 10 : и 30 символьные уникально