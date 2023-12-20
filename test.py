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

def kontrolli():
        global elud
        
        sisestatud_täht = sõna_pakkumiskast.get()
        
        if elud <= 0: 
            message_label.config(text="Kaotasid mängu", font=("Helvetica", 16), fg="#90EE90")
            return
        
        if not sisestatud_täht.isalpha():
            message_label.config(text=f"{sisestatud_täht} ei ole täht", font=("Helvetica", 16), fg="white")
            return
        if len(sisestatud_täht) != 1:
            message_label.config(text=f"{sisestatud_täht} on rohkem kui üks täht", font=("Helvetica", 16), fg="white")
            return
        
        if sisestatud_täht in arvad_sõna:
            message_label.config(text=f"Oled juba proovinud {sisestatud_täht} tähte")
        elif sisestatud_täht not in mängusõna:
            message_label.config(text=f"panid tähe '{sisestatud_täht}' valesti", font=("Helvetica", 16), fg="white")
    

        if sisestatud_täht in mängusõna:
            for i in range (len(mängusõna)):
                if mängusõna[i] == sisestatud_täht:
                    peidetud_sõna[i] = sisestatud_täht
                    message_label.config(text=f"panid tähe '{sisestatud_täht}' õigesti", font=("Helvetica", 16), fg="white")

            ekraanil_peidetud_sõna.config(text=" ". join(peidetud_sõna))

            arvad_sõna.append(sisestatud_täht)

        if sisestatud_täht not in arvad_sõna:
            arvad_sõna.append(sisestatud_täht)
            elud -= 1
            if elud > 0:
                label.config(text=pilt[7 - elud])
                
            
        if set(peidetud_sõna) == set(mängusõna):
            message_label.config(text="VÕITSID!", font=("Helvetica", 16), fg="#90EE90")
            return
        
def mäng_algab():             #enamus mängust peaks siin sees olema? äkki
    global elud, peidetud_sõna, arvad_sõna, mängusõna, sõna_pakkumiskast, message_label, ekraanil_peidetud_sõna, label
  



    sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
        "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

    mängusõna = random.choice(sõnad)  #valib mingi sõna üleval olevast listist
    mängusõna1 = list(mängusõna)
    elud = 7
    peidetud_sõna = list("_" * len(mängusõna))  #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
    arvad_sõna = []
    #--------------------------------------
    aken.destroy()  
                #siit hakkab tegelikult käima
    global mäng
                #see paneb eelmise akna kinni ja avab uue

    mäng = tk.Tk()
    mäng.title("Poomismäng")
    mäng.geometry("800x600")
    mäng.configure(bg="pink")

    font = ("Helvetica", 16)
    label = tk.Label(mäng, text=pilt[0], font=font, bg="pink", fg="#FF1493")
    label.pack(pady=10)
    label.place(relx=0.5, rely=0.3, anchor="center")

    ekraanil_peidetud_sõna = tk.Label(mäng, text = peidetud_sõna, font=font, bg="pink", fg="#FF1493")
    ekraanil_peidetud_sõna.place(relx=0.5, rely=0.5, anchor="center")

    sõna_pakkumiskast = tk.Entry(mäng, bg="#D3D3D3", fg="#FF1493")
    sõna_pakkumiskast.place(relx=0.5, rely=0.6, anchor="center")

    message_label = tk.Label(mäng, text="", bg="pink", fg="#FF1493")
    message_label.place(relx=0.5, rely=0.7, anchor="center")


    sõna_pakkumiskasti_kontroll = tk.Button(mäng, text="Paku", command=kontrolli, bg="#D3D3D3", fg="#FF1493" )
    sõna_pakkumiskasti_kontroll = tk.Button(mäng, text="Paku", command=kontrolli, bg="#D3D3D3", fg="#FF1493")
    sõna_pakkumiskasti_kontroll.place(relx=0.6, rely=0.6, anchor="center")
    

    mäng_kinni = tk.Button(mäng, text="Annan alla 🙁", command=alusta_uuesti,font=font, bg="#D3D3D3", fg="#FF1493")
    mäng_kinni.place(relx=0.5, rely=0.8, anchor="center")

    mäng.mainloop()




#----------------------------------------------------------------
#SIIN ON SEE MAIN ASI, MIS HAKKAB JOOKSMA KOHE KUI PANED ASJA TÖÖLE
    
def algus():
    global aken
    aken = tk.Tk()      #see avab akna

    aken.title("Poomismäng")  #akna nimi

    aken.geometry("800x600") #akna suurus

    aken.configure(bg="pink")


    label = tk.Label(aken, text="Mängime poomist?", font=("Helvetica", 20), bg="pink", fg="#FF007F")
    label.place(relx=0.5, rely=0.4, anchor="center")    #see nö prindib selle teksti kasti

    nupp = tk.Button(aken, text="Mängi", command=mäng_algab, bg="#D3D3D3", fg="#FF1493")  #see on nupp esmase kasti sees ja command paneb tööle mäng_algab funktsiooni, mis teeb uue akna, kus mäng on
    nupp.place(relx=0.5, rely=0.5, anchor="center")



    aken.mainloop() #see on mingi tähtis command vist aga ma täpselt ei saa aru mis teeb

def alusta_uuesti():            #viib tagasi esimesele aknale
    global mäng
    mäng.destroy()
    algus()
    
    


algus()            #siin on kõigekõige algus




    