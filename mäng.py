import random
import time

pilt = ["""
          -------
          |     |
          |
          |
          |
          |
          |
          |
          ---
          """, """
          -------
          |     |
          |     0
          |
          |
          |
          |
          |
          -------
          """,
           """
          -------
          |     |
          |     0
          |     |
          |     |
          |
          |
          |
          -------
          """,
          """
          -------
          |     |
          |     0
          |     |
          |     |
          |    /
          |
          |
          -------
          """,
          """
          -------
          |     |
          |     0
          |     |
          |     |
          |    / \\
          |
          |
          -------
          """,
          """
          -------
          |     |
          |     0
          |   --|
          |     |
          |    / \\
          |
          |
          -------
          """,
          """
          -------
          |     |
          |     0
          |   --|--
          |     |
          |    / \\
          |
          |
          -------
          """
          
          
          ]

def alusta_algusest():
    sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
            "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

    mängusõna = random.choice(sõnad)#valib mingi sõna üleval olevast listist
    mängusõna1 = list(mängusõna)
    elud = 7
    peidetud_sõna = list("_" * len(mängusõna))  #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
    arvad_sõna = ''
    õige_sõna = ''
    print("Mängime poomist!")
    print("Sul on 7 võimalust valesti pakkuda")

    print(mängusõna, elud)

    return mängusõna, mängusõna1, peidetud_sõna, elud, arvad_sõna, õige_sõna
    


mängusõna, mängusõna1, peidetud_sõna, elud, arvad_sõna, õige_sõna = alusta_algusest()

while True:
    try:
        
        if elud <= 0:
            print("Sa kaotasid")
            print("Õige sõna oli", mängusõna)
            print("Kas tahad uuesti mängida?") #lisasin et sobib nii Jah kui ka jah kui ka JAH
            vastus = input("Jah / Ei: ").lower()
            if vastus == "ei":
                break
            else:
                mängusõna, mängusõna1, peidetud_sõna, elud, arvad_sõna, õige_sõna
                continue
                

        print(pilt[7-elud])

        print ("Arva sõna ära!: ", end="")
        for i in peidetud_sõna:
            print(i, end="")
        print()
        
        

        täht = input("Paku tähte!: ").lower()
        
        if not täht.isalpha():
            print(täht, "ei ole täht")
            continue
        elif len(täht) != 1:
            print(täht, "on rohkem kui üks täht")
            continue
        elif täht in arvad_sõna:
            print("Oled juba proovinud", täht, "tähte")
            continue
           
        
        if täht in mängusõna:
            for i in range (len(mängusõna)):
                if mängusõna[i] == täht:
                    peidetud_sõna[i] = täht
 
            õige_sõna += täht #nende kaugus üli tähtis!
            arvad_sõna += täht #vajalik kuna, muidu kui paned õiget tähte 2x jookseb errorisse

        if täht not in mängusõna:
            elud -= 1
            arvad_sõna += täht
            

        if set(õige_sõna) == set(mängusõna):
            print(mängusõna)
            print("Tubli! Võitsid!")
            print("Kas tahad uuesti mängida?: ")
            vastus = input("Jah / Ei: ").lower()
            if vastus == "jah":
            
                mängusõna, mängusõna1, peidetud_sõna, elud, arvad_sõna, õige_sõna
                
                
                continue
            else:
                break
            


    except:
        print("Proovi uuesti")





