fayl_hajmi = int(input("Fayl hajmini kiriting: "))
tezlik_mbs = int(input("Internet tezligini kiriting: "))
vaqt = (fayl_hajmi*8)/tezlik_mbs
print(f"Fayl {vaqt} soniyada yuklanadi")