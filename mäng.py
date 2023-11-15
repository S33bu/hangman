import random
import time

pilt = ["""
          -------
          |		|
          |
          |
          |
          |
          |
          |
          -------
          """, """
           -------
          |		|
          |		0
          |
          |
          |
          |
          |
          -------
          """,
          """
          -------
          |		|
          |		0
          |		|
          |		|
          |
          |
          |
          -------
          """,
          """
          -------
          |		|
          |		0
          |		|
          |		|
          |	   /
          |
          |
          -------
          """,
          """
          -------
          |		|
          |		0
          |		|
          |		|
          |	   / \
          |
          |
          -------
          """,
          """
          -------
          |		|
          |		0
          |	  --|
          |		|
          |	   / \
          |
          |
          -------
          """,
          """
          -------
          |		|
          |		0
          |	  --|--
          |		|
          |	   / \
          |
          |
          -------
          """
          
          
          ]

sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
          "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

mängusõna = random.choice(sõnad) #valib mingi sõna üleval olevast listist
mängusõna1 = list(mängusõna)
elud = 7
peidetud_sõna = len(mängusõna) * "_" #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
peidetud_sõna1 = list(peidetud_sõna)
arvad_sõna = ""

print("Mängime poomist!")
print("Sul on 6 võimalust valesti pakkuda")

print(mängusõna, elud)

while True:
    try:
        
        if elud <= 0:
            print("Sa kaotasid")
            print("Kas tahad uuesti mängida? (Jah / Ei)")
            if input("(Jah / Ei)") == "Ei":
                break
            else:
                elud = 7
                mängusõna = random.choice(sõnad)

        if elud == 7:
            print(pilt[0])
        elif elud == 6:
            print(pilt[1])
        elif elud == 5:
            print(pilt[2])
        elif elud == 4:
            print(pilt[3])
        elif elud == 3:
            print(pilt[4])
        elif elud == 2:
            print(pilt[5])
        elif elud == 1:
            print(pilt[6])

        print ("Arva sõna ära!: ", end="")
        for i in peidetud_sõna1:
            print(i, end="")
        print()
        

        try:
            täht = input("Paku tähte!: ")
        except:
            print("Sisesta ainult täht")
        if not täht.isalpha():
            print("Sisesta ainult TÄHT!")
            continue
        elif len(täht) != 1:
            print("Sisesta ainult ÜKS täht!")
            continue
        if täht in mängusõna:
            for i in range (len(mängusõna)):
                if mängusõna1[i] == täht:
                    peidetud_sõna1[i] = täht

        if täht not in mängusõna:
            elud -= 1

        if peidetud_sõna1 == mängusõna1:
            print("Tubli! Võitsid!")
            print("Kas tahad uuesti mängida?: ")
            if input("Jah / Ei") == "Jah":
                elud = 7
                continue


    except:
        print("Proovi uuesti")




