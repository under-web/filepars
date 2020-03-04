import os
import re



doo = os.walk('D:\\test_directory') # указываем нужную директорию 

lst = [] # создаем пустой список

for root, dirs, files in doo:	#создаем цикл для выявления нужных файлов с расширением html (например)
	for f in files: 
		if f.endswith('.html'):   # если файл html то добавляем его в список
			lst.append(f)         # добавили в конец списка
		else:
			pass                  # если другое расширение пасуем

print(len(lst))  # выводим количество елементов списка

v = 0
vn = 0
for h in lst: # цикл для списка 
	                                          # обьединяем путь с именами из списка для дальнейшей с ним работы (передачи в функцию в которой будет выполняться работа по поиску нужной инфы по его полному пути к файлу)
	try:
		s = 'D:\\test_directory\\' + h
		
		dani = open(s, encoding='utf8').read()
		
		result = re.findall(r':\w{10,40}', dani)
		
		with open('road_in_list.txt', 'a', encoding='utf8') as wr: # метод для записи в файл в режиме добавления
			wr.write(str(result ) + '\n')
		
		print('ок', v)
		v += 1
	except:
		print('not ok', vn)
		dani = 0
		result = 0
		vn += 1
# упорядочили данные
data_analiz = open('road_in_list.txt', encoding='utf8').read()
#data_analiz = list(data_analiz)
data = set(data_analiz.split(',')) # удалили дубликаты с помощью множества
for n in data:
	print(n) 
# нужно доработать чтобы записывала сразу с магнетом














