import tkinter as tk
import random
import time

#hakka lugema sellest rohelisest joonest allpool olevast tekstist

aken = None                 #gpt ytles et ma paneks selle, siis saab mäng_algab funktsioon aru, et eelmine aken kinni panna
mäng = None
elud = 0
peidetud_sõna = []
arvad_sõna = []




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
    global elud, peidetud_sõna, arvad_sõna
  
    while elud > 0:
        kontrolli() 

    def kontrolli():
        global elud
        
        sisestatud_täht = sõna_pakkumiskast.get()
        
        if elud <= 0: 
            message_label.config(text="Kaotasid mängu", font=("Helvetica", 16), fg="red")
            return
        
        if not sisestatud_täht.isalpha():
            message_label.config(text=f"{sisestatud_täht} ei ole täht")
        if len(sisestatud_täht) != 1:
            message_label.config(text=f"{sisestatud_täht} on rohkem kui üks täht")
        if sisestatud_täht in arvad_sõna:
            message_label.config(text=f"Oled juba proovinud {sisestatud_täht} tähte")
    

        if sisestatud_täht in mängusõna:
            for i in range (len(mängusõna)):
                if mängusõna[i] == sisestatud_täht:
                    peidetud_sõna[i] = sisestatud_täht
                    message_label.config(text=f"panid tähe '{sisestatud_täht}' õigesti", font=("Helvetica", 16), fg="white")

            ekraanil_peidetud_sõna.config(text=" ". join(peidetud_sõna))

            arvad_sõna.append(sisestatud_täht)

        if sisestatud_täht not in arvad_sõna:
            message_label.config(text=f"panid tähe '{sisestatud_täht}' valesti", font=("Helvetica", 16), fg="white")
            arvad_sõna.append(sisestatud_täht)
            elud -= 1
            if elud > 0:
                label.config(text=pilt[7 - elud])
                
            
        if set(peidetud_sõna) == set(mängusõna):
            message_label.config(text="VÕITSID!", font=("Helvetica", 16), fg="green")
            return



    sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
        "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

    mängusõna = random.choice(sõnad)  #valib mingi sõna üleval olevast listist
    mängusõna1 = list(mängusõna)
    elud = 7
    peidetud_sõna = list("_" * len(mängusõna))  #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
    arvad_sõna = []
    #--------------------------------------

    global aken             #siit hakkab tegelikult käima
    global mäng
    aken.destroy()              #see paneb eelmise akna kinni ja avab uue

    mäng = tk.Tk()
    mäng.title("Poomismäng")
    mäng.geometry("800x600")
    mäng.configure(bg="#FF1493")

    font = ("Helvetica", 16)
    label = tk.Label(mäng, text=pilt[0], font=font, bg="#FF1493")
    label.pack(pady=10)

    ekraanil_peidetud_sõna = tk.Label(mäng, text = peidetud_sõna, font=font, bg="#FF1493")
    ekraanil_peidetud_sõna.pack()

    sõna_pakkumiskast = tk.Entry(mäng, bg="#FF1493")
    sõna_pakkumiskast.pack()

    message_label = tk.Label(mäng, text="", bg="#FF1493")
    message_label.pack()

    sõna_pakkumiskasti_kontroll = tk.Button(mäng, text="Paku", command=kontrolli, bg="#FF1493" )
    sõna_pakkumiskasti_kontroll.pack()
    

    mäng_kinni = tk.Button(mäng, text="Annan alla 🙁", command=alusta_uuesti,font=font, bg="#FF1493")
    mäng_kinni.pack()


    





#----------------------------------------------------------------
#SIIN ON SEE MAIN ASI, MIS HAKKAB JOOKSMA KOHE KUI PANED ASJA TÖÖLE
    
def algus():
    global aken
    aken = tk.Tk()      #see avab akna

    aken.title("Poomismäng")  #akna nimi

    aken.geometry("800x600") #akna suurus

    aken.configure(bg="pink")

    label = tk.Label(aken, text="Mängime poomist?", font=("Helvetica", 20), bg="pink")
    label.place(relx=0.5, rely=0.4, anchor="center")    #see nö prindib selle teksti kasti

    nupp = tk.Button(aken, text="Mängi", command=mäng_algab, bg="#FF1493")  #see on nupp esmase kasti sees ja command paneb tööle mäng_algab funktsiooni, mis teeb uue akna, kus mäng on
    nupp.place(relx=0.5, rely=0.5, anchor="center")



    aken.mainloop() #see on mingi tähtis command vist aga ma täpselt ei saa aru mis teeb

def alusta_uuesti():            #viib tagasi esimesele aknale
    global mäng
    mäng.destroy()
    algus()
    


algus()            #siin on kõigekõige algus




    