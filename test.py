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


def mäng_algab():             #enamus mängust peaks siin sees olema? äkki
    global elud
    global õige_sõna
    global arvad_sõna

    def kontrolli():
        sisestatud_täht = sõna_pakkumiskast.get()
        ekraanil_peidetud_sõna.config(text=sisestatud_täht)
        
        
        if not sisestatud_täht.isalpha():
            message_label.config(text=f"{sisestatud_täht} ei ole täht")
        elif len(sisestatud_täht) != 1:
            message_label.config(text=f"{sisestatud_täht} on rohkem kui üks täht")
        elif sisestatud_täht in arvad_sõna:
            message_label.config(text=f"Oled juba proovinud {sisestatud_täht} tähte")
            
        
        if sisestatud_täht in mängusõna:
            for i in range (len(mängusõna)):
                if mängusõna[i] == sisestatud_täht:
                    ekraanil_peidetud_sõna[i] = sisestatud_täht

            õige_sõna += sisestatud_täht #nende kaugus üli tähtis!
            arvad_sõna += sisestatud_täht #vajalik kuna, muidu kui paned õiget tähte 2x jookseb errorisse

        if sisestatud_täht not in mängusõna:
            global elud
            elud -= 1
            arvad_sõna += sisestatud_täht
            

        if set(õige_sõna) == set(mängusõna):
            print(mängusõna)



    sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
        "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

    mängusõna = random.choice(sõnad)  #valib mingi sõna üleval olevast listist
    mängusõna1 = list(mängusõna)
    elud = 7
    peidetud_sõna = list("_" * len(mängusõna))  #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _

    
    #--------------------------------------

    global aken             #siit hakkab tegelikult käima
    global mäng
    aken.destroy()              #see paneb eelmise akna kinni ja avab uue

    mäng = tk.Tk()
    mäng.title("Poomismäng")
    mäng.geometry("800x600")

    font = ("Helvetica", 16)
    font2 =(16)
    label = tk.Label(mäng, text=pilt[0], font=font)
    label.pack(pady=10)

    ekraanil_peidetud_sõna = tk.Label(mäng, text = peidetud_sõna, font=font)
    ekraanil_peidetud_sõna.pack()

    sõna_pakkumiskast = tk.Entry(mäng)
    sõna_pakkumiskast.pack()

    message_label = tk.Label(mäng, text="")

    sõna_pakkumiskasti_kontroll = tk.Button(mäng, text="Paku", command=kontrolli)
    sõna_pakkumiskasti_kontroll.pack()
    

    mäng_kinni = tk.Button(mäng, text="Annan alla :(", command=alusta_uuesti,font=font)
    mäng_kinni.pack()

    

    while elud > 0:
        kontrolli()




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




    