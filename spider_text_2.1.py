import os
import re



doo = os.walk('D:\\hhhoooo') # указываем нужную директорию 

lst = [] # создаем пустой список

for root, dirs, files in doo:	#создаем цикл для выявления нужных файлов с расширением html (например)
	for f in files: 
		if f.endswith('.html'):   # если файл html то добавляем его в список
			lst.append(f)         # добавили в конец списка
		else:
			pass                  # если другое расширение пасуем

print(len(lst))  # выводим количество елементов списка



for h in lst: # цикл для списка 
	s = 'D:\\hhhooo\\out\\' + h # обьединяем путь с именами из списка для дальнейшей с ним работы (передачи в функцию в которой будет выполняться работа по поиску нужной инфы по его полному пути к файлу)
	dani = open(s, encoding='utf8').read()
	result = re.findall(r':\w{10,40}', dani)
	with open('road_in_list.txt', 'a', encoding='utf8') as wr: # метод для записи в файл в режиме добавления
		wr.write(str(result) + '\n') # запишем построчно
	


#криво работает поиск и запись возвращает ошибку возможно связано с именем или некоректным путем к файлу?
