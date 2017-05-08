#Lokaverkefni - Hrútaspil
#Stefán Elís Beck
#Eyjólfur Júlíus
#dags 05.05.17 (Klárað)
from random import *
#Texta skjaið er opnað sem skra.
with open("hrutar.txt","r",encoding="utf-8") as skra:
    faersla = skra.read().split("\n")
#Spilin eru skipt í tvo jafna hluta og stokkuð.
stokka = sample(range(52),52)
#Hérna erum við að passa að allt skiptist jafnt og gerum tvo lista: Leikmadurtolur og tolvatolur
leikmadurtolur = []
tolvatolur = []
#Við klárum að stokka og látum jafnt í báða listana
#Ef við látum þetta ekki inn þá segir kóðinn að tölvan hafi unnið með engri útskýringu
for i in stokka:
    if i%2 == 0:
        tolvatolur.append(i)
    else:
        leikmadurtolur.append(i)
#Hér búum við til spilalistana leikmadur, tolva og jafntefli.
leikmadur = []
tolva = []
jafntefli = []
#Hér fara tölurnar í færsluna hjá leikmann og tölvu.
for i in leikmadurtolur:
    leikmadur.append(faersla[i])
for i in tolvatolur:
    tolva.append(faersla[i])
#Hér er While lykkjan sem heldur leiknum gangandi.
while len(leikmadur)>0 and len(tolva)>0:
#Hér er skrifað út hver á leikinn og spilin hans.
    print("Leikmaður á leik")
    print(leikmadur)
#Hér er að splitta spilinu í nafn og flokka.
    spil1 = leikmadur[0].split(":")
    spil2 = tolva[0].split(":")
#Hér er prent út flokkana
    print("Flokkarnir")
    print("1 - Þyngd (kg)")
    print("2 - Mjólkurlagni (dætra)")
    print("3 - Einkunn ullar")
    print("4 - Fjöldi afkvæma")
    print("5 - Einkunn læris")
    print("6 - Frjósemi")
    print("7 - Gerð/þykkt bakvöðva")
    print("8 - Einkun fyrir malir")
    print("Þetta er spilið þitt")
#Hér er prentað út efsta spilið
    print(spil1)
#Hér fær notandinn að velja hvaða flokk hann vill nota
    val = int(input("Hvaða flokk viltu nota? "))
    flokkarspil1 = spil1[1].split(",")
    print(flokkarspil1[val-1])
    flokkarspil2 = spil2[1].split(",")
#Ef notandi vinnur
    if float(flokkarspil1[val-1]) > float(flokkarspil2[val-1]):
        print("Þú vannst!")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(tolva[0])
        tolva.remove(tolva[0])
        print(leikmadur)
#Ef tolvan vinnur
    elif float(flokkarspil2[val-1]) > float(flokkarspil1[val-1]):
        print("Tölvan vann!")
        if len(jafntefli)>0:
            for spil in jafntefli:
                tolva.append(spil)
            jafntefli.clear()
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        tolva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        print(leikmadur)
#Ef það verður jafntefli
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(tolva[0])
        leikmadur.remove(leikmadur[0])
        tolva.remove(tolva[0])
        print(jafntefli)
#Nú á tolvan leik
    print("tolvan á leik")
    val = randint(0,7)
    flokkarspil1 = spil1[1].split(",")
    flokkarspil2 = spil2[1].split(",")
    jafntefli = []
#Ef notandi vinnur
    if float(flokkarspil1[val]) > float(flokkarspil2[val]):
        print("Þú vannst")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(tolva[0])
        tolva.remove(tolva[0])
        print(leikmadur)
#Ef tolvan vinnur
    elif float(flokkarspil2[val]) > float(flokkarspil1[val]):
        print("tolvan vann")
        if len(jafntefli)>0:
            for spil in jafntefli:
                tolva.append(spil)
            jafntefli.clear()
        tolva.append(jafntefli)
        tolva.append(tolva[0])
        tolva.remove(tolva[0])
        tolva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        print(leikmadur)
#Ef það verður jafntefli
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(tolva[0])
        print(jafntefli)

#Nú er einhver sigurvegari og skrifað er út hver vann.
if len(leikmadur) == 0:
    print("tolvan vann leikinn!")
    print("Takk fyrir leikinn :)")
elif len(tolva) == 0:
    print("Þú vannst leikinn!")
    print("Takk fyrir leikinn :)")