import random

pildid = []

sõnad = ["õun", "jõgi", "laud", "kott", "nupp", "uks", "käsi",
          "kell", "tuli", "rohi", "nina", "lill", "tore", "pilt", "päev"]

mängusõna = random.choice(sõnad) #valib mingi sõna üleval olevast listist
mängusõna1 = list(mängusõna)
elud = len(mängusõna) #elusid on sama palju kui tähti sõnas
peidetud_sõna = len(mängusõna) * "_" #siin nt kui sõna on kott ja sa pakud k siis -> k _ _ _
peidetud_sõna1 = list(peidetud_sõna)

print(mängusõna, elud)

while elud > 0:
    print ("Arva sõna ära!: ", end="")
    for i in peidetud_sõna1:
        print(i, end="")
    print()
    täht = input("Paku tähte!: ")
    if täht in mängusõna:
        for i in range (len(mängusõna)):
            if mängusõna1[i] == täht:
                peidetud_sõna1[i] = täht
