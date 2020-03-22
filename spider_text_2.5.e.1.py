
import os
import re

#Дописать функциональную версию


path = 'D:\\test_directory' 

lst = []                                    # создаем пустой список

v = 0
vn = 0


directory = os.walk(path) # указываем нужную директорию 

for root, dirs, files in directory:	#создаем цикл для выявления нужных файлов с расширением html (например)
	for f in files: 
		if f.endswith('.html'):   # если файл html то добавляем его в список
			lst.append(f)         # добавили в конец списка
		else:
			pass                  # если другое расширение пасуем

print(len(lst))                    # выводим количество елементов списка


for h in lst:                          # цикл для списка 
	                                          # обьединяем путь с именами из списка для дальнейшей с ним работы (передачи в функцию в которой будет выполняться работа по поиску нужной инфы по его полному пути к файлу)
	try:
		s = path + '\\' + h    # создаем путь понятный системе для каждого файла
		
		page = open(s, encoding='utf8').read() # передали переменной содержимое первого элемента(файла) открыв в режиме чтения  
		
		result = re.findall(r':\w{10,40}', page) # ищем в открытом файле нужную информацию через ключевые слова
		
		with open('newout.txt', 'a', encoding='utf8') as wr: # метод для записи в файл в режиме добавления
			wr.write(str(result ) + '\n') # записываем содержимое переменной result в новый файл тхт 
		
		print('ок', v) # отображение состояния
		v += 1
	except:
		print('not ok', vn)
		dani = 0
		result = 0
		vn += 1

data_analiz = open('newout.txt', encoding='utf8').read()
stan = re.findall(r':\w{10,40}', data_analiz) # убераем совпадения (одинаковые данные) множествами set
stan = set(stan)
for x in stan:
	with open('total_out.txt', 'a', encoding='utf8') as gr:
		gr.write('magnet:?xt=urn:btih' + x + '\n')

print()
print()
print('Общее количество файлов:   ' + str(len(lst)))
print()
print('Количество найденных ссылок:   ' + str(len(stan)))















