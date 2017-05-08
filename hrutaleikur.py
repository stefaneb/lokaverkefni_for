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