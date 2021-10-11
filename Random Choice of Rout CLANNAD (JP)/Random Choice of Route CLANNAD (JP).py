# -*- coding: utf-8 -*- 


logo='''
 ____________________________________________________
|                                                    |
|   [--] Name: Random Choice of Route CLANNAD        |
|                                                    |
|   [--] Author: Oleksenko Ivan  (IPOleksenko)       |
|                                                    |
|   [--] Language: Japanese                          |
|                                                    |
|   [--] Thank studio "KEY" for CLANNAD.             |
|____________________________________________________|
'''

text='''
含まれているエンディング:{}
エンディング After Story 含まれている:{}
無効になっているエンディング:{}
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
	res1=input ('ルート書き込みをランダムに選択するには "1"\nパスを選択するには"After Story" 書く "2"\nいくつかのエンディングを無効/有効にしたい場合は書き込み "0"\n>')
	
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

	res2= input('選択を変更します - "1"\nスタートメニューに戻る - "2"\n>')

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
		res3= input('選択を変更したい場合は、 "1"\n前の選択を変更するには、 "2"\n>')
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
	Her=input('書く "1" ランダムにエンディングをオフにしたい場合\n書く "2" エンディングをランダムに含めたい場合\n書く "3" すべての変更を元に戻したい場合\n書く "0" 終了オプションの編集が終了した場合\n>')
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
	SS=input('書く "0" メインメニューに戻る\n書く "1" 無効にするには "Misae Route"\n書く "2" 無効にするには "Tomoyo Route"\n書く "3" 無効にするには "Yukine Route"\n書く "4" 無効にするには "Kyou Route"\n書く "5" 無効にするには "Ryou Route"\n書く "6" 無効にするには "Kappei Route"\n書く "7" 無効にするには "Mei Route"\n書く "8" 無効にするには "Kotomi Route"\n書く "9" 無効にするには "Fuko Route"\n書く "10" 無効にするには "Koumura Route"\n書く "11" 無効にするには "Nagisa Route"\n書く "12" 無効にするには "Baseball Route"\n書く "13" 無効にするには "Sunohara’s Ending"\n書く "14" 無効にするには "Akio Route"\n書く "15" 無効にするには "After Story"\n書く "16" 無効にするには "True End"\n>')
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
	SSAS=input('書く "0" メインメニューに戻る\n書く "1" 電源を入れる "Misae Route"\n書く "2" 電源を入れる "Tomoyo Route"\n書く "3" 電源を入れる "Yukine Route"\n書く "4" 電源を入れる "Kyou Route"\n書く "5" 電源を入れる "Ryou Route"\n書く "6" 電源を入れる "Kappei Route"\n書く "7" 電源を入れる "Mei Route"\n書く "8" 電源を入れる "Kotomi Route"\n書く "9" 電源を入れる "Fuko Route"\n書く "10" 電源を入れる "Koumura Route"\n書く "11" 電源を入れる "Nagisa Route"\n書く "12" 電源を入れる "Baseball Route"\n書く "13" 電源を入れる "Sunohara’s Ending"\n書く "14" 電源を入れる "Akio Route"\n書く "15" 電源を入れる "After Story"\n書く "16" 電源を入れる "True End"\n>')
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
