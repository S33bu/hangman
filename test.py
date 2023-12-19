import tkinter as tk
import random
import time

#hakka lugema sellest rohelisest joonest allpool olevast tekstist

aken = None                 #gpt ytles et ma paneks selle, siis saab mäng_algab funktsioon aru, et eelmine aken kinni panna
mäng = None

pilt = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",            #parem versioon pildist, iga rida on erinev elu, allpool on mängu lõpp
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]


def mäng_algab():               #enamus mängust peaks siin sees olema? äkki
    
    sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
        "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

    mängusõna = random.choice(sõnad)  #valib mingi sõna üleval olevast listist
    mängusõna1 = list(mängusõna)
    elud = 7
    peidetud_sõna = list("_" * len(mängusõna))  #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
    arvad_sõna = ''
    õige_sõna = ''
    
    #--------------------------------------

    global aken             #siit hakkab tegelikult käima
    global mäng
    aken.destroy()              #see paneb eelmise akna kinni ja avab uue

    mäng = tk.Tk()
    mäng.title("Poomismäng")
    mäng.geometry("800x600")

    font = ("Helvetica", 16)
    label = tk.Label(mäng, text=pilt[6], font=font)
    label.pack(pady=10)

    ekraanil_peidetud_sõna = tk.Label(mäng, text = peidetud_sõna, font=font)
    ekraanil_peidetud_sõna.pack(pady=10)

    sõna_pakkumiskast = tk.Entry(mäng)
    sõna_pakkumiskast.pack(pady=10)

    mäng_kinni = tk.Button(mäng, text="Annan alla :(", command=alusta_uuesti)
    mäng_kinni.pack(pady=40)

    sisestatud_sõna = sõna_pakkumiskast.get()
    print("kirjutasid: ", sisestatud_sõna)

#----------------------------------------------------------------
#SIIN ON SEE MAIN ASI, MIS HAKKAB JOOKSMA KOHE KUI PANED ASJA TÖÖLE
    
def algus():
    global aken
    aken = tk.Tk()      #see avab akna

    aken.title("Poomismäng")  #akna nimi

    aken.geometry("800x600") #akna suurus

    label = tk.Label(aken, text="Mängime poomist?")
    label.pack()    #see nö prindib selle teksti kasti

    nupp = tk.Button(aken, text="Mängi", command=mäng_algab)  #see on nupp esmase kasti sees ja command paneb tööle mäng_algab funktsiooni, mis teeb uue akna, kus mäng on
    nupp.pack()



    aken.mainloop() #see on mingi tähtis command vist aga ma täpselt ei saa aru mis teeb

def alusta_uuesti():            #viib tagasi esimesele aknale
    global mäng
    mäng.destroy()
    algus()
    


algus()         #siin on kõigekõige algus




    