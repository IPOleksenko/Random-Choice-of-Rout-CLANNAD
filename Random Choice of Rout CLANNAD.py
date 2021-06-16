# -*- coding: utf-8 -*- 
from tkinter import *
import random
logo='''                                                  
[--] Name: Random Choice of Route CLANNAD        
[--] Author: Oleksenko Ivan  (IPOleksenko)                                        
[--] Thank studio "KEY" for CLANNAD.             
'''
def peremen():
    Misr="Сагара Мисае"
    Tomr="Сакагами Томоё"
    Miyr="Миязава Юкинэ"
    Ker="Кё Фудзибаяси"
    Rer="Рё Фудзибаяси"
    Xyir="Хиираги Каппей"
    Sisr="Мей Сунохара"
    Kotr="Ичиносэ Котоми"
    Ibr="Фуко Ибуки"
    Komr="Коумура Тосио"
    Fur="Нагиса Фурукава"
    Beyr="Бейсбол"
    Yaor="Путь Сунохары"
    global selectpersonr
    selectpersonr= [Misr, Tomr, Miyr, Ker, Rer, Xyir, Sisr, Kotr, Ibr, Komr, Fur, Beyr, Yaor]
    Akr=("Путь Акио")
    Gpr=("Главный путь")
    Isr=("Истиная концовка")
    global selectperson2r
    selectperson2r=[Akr, Gpr, Isr]
    Mise="Misae Route"
    Tome="Tomoyo Route"
    Miye="Yukine Route"
    Kee="Kyou Route"
    Ree="Ryou Route"
    Xyie="Kappei Route"
    Sise="Mei Route"
    Kote="Kotomi Route"
    Ibe="Fuko Route"
    Kome="Koumura Route"
    Fue="Nagisa Route"
    Beye="Baseball Route"
    Yaoe="Sunohara’s Ending"
    global selectpersone
    selectpersone= [Mise, Tome, Miye, Kee, Ree, Xyie, Sise, Kote, Ibe, Kome, Fue, Beye, Yaoe]
    Ake=("Akio Route")
    Gpe=("After Story")
    Ise=("True End")
    global selectperson2e
    selectperson2e=[Ake, Gpe, Ise]
    Misj="Misae Route"
    Tomj="Tomoyo Route"
    Miyj="Yukine Route"
    Kej="Kyou Route"
    Rej="Ryou Route"
    Xyij="Kappei Route"
    Sisj="Mei Route"
    Kotj="Kotomi Route"
    Ibj="Fuko Route"
    Komj="Koumura Route"
    Fuj="Nagisa Route"
    Beyj="Baseball Route"
    Yaoj="Sunohara’s Ending"
    global selectpersonj
    selectpersonj= [Misj, Tomj, Miyj, Kej, Rej, Xyij, Sisj, Kotj, Ibj, Komj, Fuj, Beyj, Yaoj]
    Akj=("Akio Route")
    Gpj=("After Story")
    Isj=("True End")
    global selectperson2j
    selectperson2j=[Akj, Gpj, Isj]
    global REPRUS
    global REPJPN
    global REPENG
    global RandA
    global Rand
    global RandAj
    global Randj
    global RandAe
    global Rande
    REPENG= Button(
        text= 'Return',
        command= ENGrep
        )
    REPRUS= Button(
        text= 'Назад',
        command= RUSrep
        )
    REPJPN= Button(
        text= '戻る',
        command= JPNrep
        )
    RandA=Label(
        text= random.choice(selectperson2r)
        )
    Rand=Label(
        text= random.choice(selectpersonr)
        )
    RandAe=Label(
        text= random.choice(selectperson2e)
        )
    Rande=Label(
        text= random.choice(selectpersone)
        )
    Randj=Label(
        text= random.choice(selectpersonj)
        )
    RandAj=Label(
        text= random.choice(selectperson2j)
        )
    global retuurnj
    retuurnj= Button(text=('最初'),
    command=startj
    )
    retuurnj.pack()
    global retuurne
    retuurne= Button(text=('First'),
    command=starte
    )
    retuurne.pack()
    global retuurnr
    retuurnr= Button(text=('С начала'),
    command=startr
    )
    retuurnr.pack()
    start()        
def RUSrep():
    Rand.pack_forget()
    RandA.pack_forget()
    REPRUS.pack_forget()
    RCA.pack_forget()
    RC.pack_forget()
    RUS()
def ENGrep():
    Rande.pack_forget()
    RandAe.pack_forget()
    REPENG.pack_forget()
    RCAe.pack_forget()
    RCe.pack_forget()
    ENG()
def JPNrep():
    Randj.pack_forget()
    RandAj.pack_forget()
    REPJPN.pack_forget()
    RCAj.pack_forget()
    RCj.pack_forget()
    JPN()
def huiiiA():
    RandA.pack_forget()
    act2ARUS()
def act2ARUS():
    retuurnr.pack_forget()
    RandA.config(
        text= random.choice(selectperson2r)
        )
    RC.pack_forget()
    st.pack_forget()
    RandA.pack()
    RCA.config(text='Ещё раз',
        command=huiiiA)
    REPRUS.pack()
def huiii():
    Rand.config(
        text= random.choice(selectperson2r)
        )
    REPRUS.pack_forget()
    Rand.pack_forget()
    act2RUS() 
def act2RUS():
    retuurnr.pack_forget()
    RCA.pack_forget()
    st.pack_forget()
    Rand.pack()
    RC.config(text='Ещё раз',
        command=huiii)
    REPRUS.pack()
def startr():
    st.pack_forget() 
    RC.pack_forget() 
    RCA.pack_forget() 
    start()    
def RUS():
    global st
    global RC
    global RCA
    TITL.pack_forget() 
    REPENG.pack_forget()
    REPRUS.pack_forget()
    REPJPN.pack_forget()
    ButtonStarte.pack_forget()
    ButtonStartj.pack_forget()
    ButtonStart.pack_forget()
    ButtonExit.pack_forget()
    st= Label(
        text=logo
        )
    st.pack()
    
    RC= Button(
        text='Концовка',
        command= act2RUS
        )
    RC.pack()
    
    RCA= Button(
        text="Продолжение истории",
        command=act2ARUS
        )
    RCA.pack()
    retuurnr.pack()
def huiiiAe():
    RandAe.pack_forget()
    act2AENG()
def act2AENG():
    retuurne.pack_forget()
    RandAe.config(
        text= random.choice(selectperson2e)
        )
    RCAe.pack_forget()
    RCe.pack_forget()
    RCe.pack_forget()
    ste.pack_forget()  
    RCAe.pack()
    RandAe.pack()
    RCAe.config(text='Again',
        command=huiiiAe)
    REPENG.pack()
def huiiie():
    REPENG.pack_forget()
    Rande.pack_forget()
    act2ENG()
def act2ENG():
    retuurne.pack_forget()
    Rande.config(
        text= random.choice(selectpersone)
        )
    RCAe.pack_forget()
    ste.pack_forget()   
    Rande.pack()
    RCe.config(text='Again',
        command=huiiie)
    REPENG.pack()
def starte():
    ste.pack_forget() 
    RCe.pack_forget() 
    RCAe.pack_forget() 
    start()    
def ENG():
    global ste
    global RCe
    global RCAe
    TITL.pack_forget() 
    ButtonStart.pack_forget()
    ButtonStarte.pack_forget()
    ButtonStartj.pack_forget()
    ButtonExit.pack_forget()
    ste= Label(
        text=logo
        )
    ste.pack()
    
    RCe= Button(
        text='Endings',
        command= act2ENG
        )
    RCe.pack()
    
    RCAe= Button(
        text="After Story",
        command=act2AENG
        )
    RCAe.pack()
    retuurne.pack()
def huiiiAj():
    REPENG.pack_forget()
    RandAj.pack_forget()
    act2AJPN()
def act2AJPN():
    retuurnj.pack_forget()
    RandAj.config(
        text= random.choice(selectperson2j)
        )
    RCj.pack_forget()
    stj.pack_forget()
    RandAj.pack()
    RCAj.config(text='再び',
        command=huiiiAj)
    REPJPN.pack()
def huiiij():
    Randj.pack_forget()
    act2JPN()
def act2JPN():
    retuurnj.pack_forget()
    Randj.config(
        text= random.choice(selectpersonj)
        )
    RCAj.pack_forget()
    stj.pack_forget()
    Randj.pack()
    RCj.config(text='再び',
        command=huiiij)
    REPJPN.pack()
def startj():
    stj.pack_forget() 
    RCj.pack_forget() 
    RCAj.pack_forget() 
    start()
def JPN():
    global stj
    global RCj
    global RCAj
    TITL.pack_forget() 
    REPENG.pack_forget()
    REPRUS.pack_forget()
    REPJPN.pack_forget()
    ButtonStart.pack_forget()
    ButtonStarte.pack_forget()
    ButtonStartj.pack_forget()
    ButtonExit.pack_forget()
    stj= Label(
        text=logo
        )
    stj.pack()
    
    RCj= Button(
        text='エンディング',
        command= act2JPN
        )
    RCj.pack()
    
    RCAj= Button(
        text="アフターストーリー",
        command=act2AJPN
        )
    RCAj.pack()
    retuurnj.pack()
def start():
    retuurnj.pack_forget()
    retuurnr.pack_forget()
    retuurne.pack_forget()
    global TITL
    TITL= Label(
        text='Language'
        )
    TITL.pack()


    global ButtonStart
    ButtonStart=Button(
        text="RUS",
        command= RUS
        )
    ButtonStart.pack()
    
    global ButtonStarte
    ButtonStarte=Button(
        text='ENG',
        command=ENG
        )
    ButtonStarte.pack()
    global ButtonStartj
    ButtonStartj=Button(
        text='JPN',
        command=JPN
        )
    ButtonStartj.pack()
    global ButtonExit
    ButtonExit= Button(
        text='EXIT',
        command= quit
        )   
    ButtonExit.pack()
menu= Tk()
menu.resizable(width=False, height=False)
menu.title('Random Choice of Rout CLANNAD | IPOleksenko')
menu.iconbitmap('ICON\clannad-anime-icon-clannad-png-icon-thumbnail.ico')
peremen()
menu.mainloop()