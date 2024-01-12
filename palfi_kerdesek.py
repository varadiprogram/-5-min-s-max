szamok = []
vege = 5
paros = 0

while vege != 0:
    szam = int(input("Szám: "))

    if szam % 2 == 0:
        paros = paros + 1

    szamok.append(szam)
    vege = vege - 1

legnagyobb_szam = max(szamok)
legkisebb_szam = min(szamok)

print(f"Ennyi szám osztható kettővel: {paros}")
print(f"legnagyobb szám: {legnagyobb_szam}\nLegkissebb szám: {legkisebb_szam}")
