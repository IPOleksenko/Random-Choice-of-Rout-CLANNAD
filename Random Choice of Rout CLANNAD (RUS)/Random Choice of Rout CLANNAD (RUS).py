# -*- coding: utf-8 -*- 


logo='''
 ____________________________________________________
|                                                    |
|   [--] Name: Random Choice of Route CLANNAD        |
|                                                    |
|   [--] Author: Oleksenko Ivan  (IPOleksenko)       |
|                                                    |
|   [--] Language: Russian                           |
|                                                    |
|   [--] Thank studio "KEY" for CLANNAD.             |
|____________________________________________________|
'''

text='''
Концовки которые включены:{}
Концовки After Story которые включены:{}
Концовки которые отключены:{}
'''

Mis="Сагара Мисае"
Tom="Сакагами Томоё"
Miy="Миязава Юкинэ"
Ke="Кё Фудзибаяси"
Re="Рё Фудзибаяси"
Xyi="Хиираги Каппей"
Sis="Мей Сунохара"
Kot="Ичиносэ Котоми"
Ib="Фуко Ибуки"
Kom="Коумура Тосио"
Fu="Нагиса Фурукава"
Bey="Бейсбол"
Yao="Путь Сунохары"
selectperson= [Mis, Tom, Miy, Ke, Re, Xyi, Sis, Kot, Ib, Kom, Fu, Bey, Yao]
selectpersonoff= []

Ak=("Путь Акио")
Gp=("Главный путь")
Is=("Истиная концовка")
selectperson2=[Ak, Gp, Is]

import random
import os

def root_choise():
	print(logo)
	res1=input ('Для случайного выбора рута напиши "1"\nДля выбора пути"Продолжение истории" напиши "2"\nЕсли хочешь отключить/включить некоторые концовки напиши "0"\n>')
	
	try:
		if res1=='1':
			os.system('cls||clear')
			rest()
		elif res1== '2':
			os.system('cls||clear')
			AS()
		elif res1=='0':
			os.system('cls||clear')
			PZD()
		else:
			os.system('cls||clear')
			root_choise()

	except:
		root_choise()

        
		
def rest():	
	try:	
		print(random.choice(selectperson))
	except:
		root_choise()
	
	a()
def a():	

	res2= input('Сменит выбор - "1"\nВозвращение в начальное меню - "2"\n>')

	if res2 =='1':
		os.system('cls||clear')
		rest()
	elif res2 =='2':
		os.system('cls||clear')
		root_choise()
	else:       
		os.system('cls||clear')
		a()
		
def AS():

		try:
			print(random.choice(selectperson2))
		except:
			root_choise()
			
		b()
def b():
	try:
		res3= input('Хочешь поменять выбор, напиши "1"\nЧто бы поменять прошлый выбор напиши "2"\n>')
		if res3 == '1':
			os.system('cls||clear')
			AS()
		elif res3 == '2':
			os.system('cls||clear')
			root_choise()
		else:
			os.system('cls||clear')
			b()
	except:
		root_choise()
def PZD():
	Her=input('Напиши "1" если хочешь отключить концовку в рандоме\nНапиши "2" если хочешь включить концовку в рандоме\nНапиши "3" если хочешь отменить все изминения\nНапиши "0" если ты закончил редактировать варианты концовак\n>')
	os.system('cls||clear')
	if Her== '0':
		root_choise()
	elif Her== '1':
		off()
	elif Her== '2':
		on()
	elif Her=='3':   
		global selectperson
		global selectperson2
		global selectpersonoff
		selectperson= [Mis, Tom, Miy, Ke, Re, Xyi, Sis, Kot, Ib, Kom, Fu, Bey, Yao]
		selectperson2= [Ak, Gp, Is]
		selectpersonoff= []
		root_choise()
	else:
		os.system('cls||clear')
		PZD()
		
def off():
	print(text.format(selectperson, selectperson2, selectpersonoff))
	SS=input('Напиши "0" чтобы вернутся в главное меню\nНапиши "1" чтобы отключить "Сакагами Мисае"\nНапиши "2" чтобы отключить "Сакагами Томоё"\nНапиши "3" чтобы отключить "Миязава Юкинэ"\nНапиши "4" чтобы отключить "Кё Фудзибаяси"\nНапиши "5" чтобы отключить "Рё Фудзибаяси"\nНапиши "6" чтобы отключить "Хиираги Каппей"\nНапиши "7" чтобы отключить "Мей Сунохара"\nНапиши "8" чтобы отключить "Ичиносе Котоми"\nНапиши "9" чтобы отключить "Фуко Ибуки"\nНапиши "10" чтобы отключить "Коумура Тосио"\nНапиши "11" чтобы отключить "Нагиса Фурукава"\nНапиши "12" чтобы отключить "Бейсбол"\nНапиши "13" чтобы отключить "Путь Сунохары"\nНапиши "14" чтобы отключить "Путь Акио"\nНапиши "15"чтобы отключить "Главный путь"\nНапиши "16" чтобы отключить "Истиная концовка"\n>')
	os.system('cls||clear')
	try:
	#Story
		if SS=='1':
			selectperson.remove(Mis)
			selectpersonoff.append(str(Mis))
		elif SS=='2':
			selectperson.remove(Tom)
			selectpersonoff.append(Tom)
		elif SS=='3':
			selectperson.remove(Miy)
			selectpersonoff.append(Miy)
		elif SS=='4':
			selectperson.remove(Ke)
			selectpersonoff.append(Ke)
		elif SS=='5':
			selectperson.remove(Re)
			selectpersonoff.append(Re)
		elif SS=='6':
			selectperson.remove(Xyi)
			selectpersonoff.append(Xyi)
		elif SS=='7':
			selectperson.remove(Sis)
			selectpersonoff.append(Sis)
		elif SS=='8':
			selectperson.remove(Kot)
			selectpersonoff.append(Kot)
		elif SS=='9':
			selectperson.remove(Ib)
			selectpersonoff.append(Ib)
		elif SS=='10':
			selectperson.remove(Kom)
			selectpersonoff.append(Kom)
		elif SS=='11':
			selectperson.remove(Fu)
			selectpersonoff.append(Fu)
		elif SS=='12':
			selectperson.remove(Bey)
			selectpersonoff.append(Bey)
		elif SS=='13':
			selectperson.remove(Yao)
			selectpersonoff.append(Yao)
			
	#AS
		elif SS=='14':
			selectperson2.remove(Ak)
			selectpersonoff.append(Ak)
		elif SS=='15':
			selectperson2.remove(Gp)
			selectpersonoff.append(Gp)
		elif SS=='16':
			selectperson2.remove(Is)
			selectpersonoff.append(Is)

		if SS != '0':
			off()
		else:
			root_choise()
	except:
		root_choise()
def on():
	print(text.format(selectperson, selectperson2, selectpersonoff))
	SSAS=input('Напиши "0" чтобы вернутся в главное меню\nНапиши "1" чтобы включить "Сакагами Мисае"\nНапиши "2" чтобы включить "Сакагами Томоё"\nНапиши "3" чтобы включить "Миязава Юкинэ"\nНапиши "4" чтобы включить "Кё Фудзибаяси"\nНапиши "5" чтобы включить "Рё Фудзибаяси"\nНапиши "6" чтобы включить "Хиираги Каппей"\nНапиши "7" чтобы включить "Мей Сунохара"\nНапиши "8" чтобы включить "Ичиносе Котоми"\nНапиши "9" чтобы включить "Фуко Ибуки"\nНапиши "10" чтобы включить "Коумура Тосио"\nНапиши "11" чтобы включить "Нагиса Фурукава"\nНапиши "12" чтобы включить "Бейсбол"\nНапиши "13" чтобы включить "Путь Сунохары"\nНапиши "14" чтобы включить "Путь Акио"\nНапиши "15"чтобы включить "Главный путь"\nНапиши "16" чтобы включить "Истиная концовка"\n>')
	os.system('cls||clear')
	try:
	#Story
		if SSAS=='1':
			selectpersonoff.remove(Mis)
			selectperson.append(Mis)
		elif SSAS=='2':
			selectpersonoff.remove(Tom)
			selectperson.append(Tom)
		elif SSAS=='3':
			selectpersonoff.remove(Miy)
			selectperson.append(Miy)
		elif SSAS=='4':
			selectpersonoff.remove(Ke)
			selectperson.append(Ke)
		elif SSAS=='5':
			selectpersonoff.remove(Re)
			selectperson.append(Re)
		elif SSAS=='6':
			selectpersonoff.remove(Xyi)
			selectperson.append(Xyi)
		elif SSAS=='7':
			selectpersonoff.remove(Sis)
			selectperson.append(Sis)
		elif SSAS=='8':
			selectpersonoff.remove(Kot)
			selectperson.append(Kot)
		elif SSAS=='9':
			selectpersonoff.remove(Ib)
			selectperson.append(Ib)
		elif SSAS=='10':
			selectpersonoff.remove(Kom)
			selectperson.append(Kom)
		elif SSAS=='11':
			selectpersonoff.remove(Fu)
			selectperson.append(Fu)
		elif SSAS=='12':
			selectpersonoff.remove(Bey)
			selectperson.append(Bey)
		elif SSAS=='13':
			selectpersonoff.remove(Yao)
			selectperson.append(Yao)
			
	#AS
		elif SSAS=='14':
			selectpersonoff.remove(Ak)
			selectperson2.append(Ak)
		elif SSAS=='15':
			selectpersonoff.remove(Gp)
			selectperson2.append(Gp)
		elif SSAS=='16':
			selectpersonoff.remove(Is)
			selectperson2.append(Is)
		if SSAS != '0':
			on()
		else:
			root_choise()
	except:
		root_choise()

if __name__=='__main__':
    while True:
    	root_choise()