# -*- coding: utf-8 -*- 


logo='''
 ____________________________________________________
|                                                    |
|   [--] Name: Random Choice of Route CLANNAD        |
|                                                    |
|   [--] Author: Oleksenko Ivan  (IPOleksenko)       |
|                                                    |
|   [--] Language: English                           |
|                                                    |
|   [--] Thank studio "KEY" for CLANNAD.             |
|____________________________________________________|
'''

text='''
Endings that are included:{}
After Story endings included:{}
Endings that are disabled:{}
'''

Mis="Misae Route"
Tom="Tomoyo Route"
Miy="Yukine Route"
Ke="Kyou Route"
Re="Ryou Route"
Xyi="Kappei Route"
Sis="Mei Route"
Kot="Kotomi Route"
Ib="Fuko Route"
Kom="Koumura Route"
Fu="Nagisa Route"
Bey="Baseball Route"
Yao="Sunohara’s Ending"
selectperson= [Mis, Tom, Miy, Ke, Re, Xyi, Sis, Kot, Ib, Kom, Fu, Bey, Yao]
selectpersonoff= []

Ak=("Akio Route")
Gp=("After Story")
Is=("True End")
selectperson2=[Ak, Gp, Is]

import random
import os

def root_choise():
	print(logo)
	res1=input ('To randomly select the rout write "1"\nTo choose a path"After Story" write "2"\nIf you want to disable / enable some endings write "0"\n>')
	
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

	res2= input('Will change the choice - "1"\nReturn to start menu - "2"\n>')

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
		res3= input('If you want to change your choice, write "1"\nTo change the previous choice, write "2"\n>')
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
	Her=input('write "1" if you want to turn off the ending in random\nwrite "2" if you want to include the ending in random\nwrite "3" if you want to undo all the changes\nwrite "0" if you\'ve finished editing the ending options\n>')
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
	SS=input('write "0" to return to the main menu\nwrite "1" to disable "Misae Route"\nwrite "2" to disable "Tomoyo Route"\nwrite "3" to disable "Yukine Route"\nwrite "4" to disable "Kyou Route"\nwrite "5" to disable "Ryou Route"\nwrite "6" to disable "Kappei Route"\nwrite "7" to disable "Mei Route"\nwrite "8" to disable "Kotomi Route"\nwrite "9" to disable "Fuko Route"\nwrite "10" to disable "Koumura Route"\nwrite "11" to disable "Nagisa Route"\nwrite "12" to disable "Baseball Route"\nwrite "13" to disable "Sunohara’s Ending"\nwrite "14" to disable "Akio Route"\nwrite "15" to disable "After Story"\nwrite "16" to disable "True End"\n>')
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
	SSAS=input('write "0" to return to the main menu\nwrite "1" to turn on "Misae Route"\nwrite "2" to turn on "Tomoyo Route"\nwrite "3" to turn on "Yukine Route"\nwrite "4" to turn on "Kyou Route"\nwrite "5" to turn on "Ryou Route"\nwrite "6" to turn on "Kappei Route"\nwrite "7" to turn on "Mei Route"\nwrite "8" to turn on "Kotomi Route"\nwrite "9" to turn on "Fuko Route"\nwrite "10" to turn on "Koumura Route"\nwrite "11" to turn on "Nagisa Route"\nwrite "12" to turn on "Baseball Route"\nwrite "13" to turn on "Sunohara’s Ending"\nwrite "14" to turn on "Akio Route"\nwrite "15" to turn on "After Story"\nwrite "16" to turn on "True End"\n>')
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
#Author: IPOleksenko
