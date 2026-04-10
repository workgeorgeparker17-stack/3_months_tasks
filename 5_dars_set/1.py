# mevalar = {"olma", "banan"}
# mevalar.add("gilos")     # Bitta element qoshadi
# # mevalar.add("Shaftoli")
# print(mevalar)


# bosh = set()  # bo'sh set 
# sonlar = {1, 2, 3, 4}
# matn = set("salom")  # har bir harf alohida element
# print(matn)


# 2.update() bir nechta elementlarni qoshadi
# mevalar = {"olma", "banan"}
# mevalar.update(["gilos", "anor", "uzum"])
# print(mevalar)


# 3.remove elementni o'chiradi
# mevalar = {"olma", "banan", "gilos"}
# mevalar.remove("banan")
# print(mevalar)
# Agar element bolmasa, Keyerror xatolik beradi



## 🔹 6. `discard()` – elementni o‘chirish (xato bermaydi)


# mevalar = {"olma", "banan"}
# mevalar.discard("gilos")  # mavjud emas, lekin xato bermaydi
# print(mevalar)

# Discard xatolik bermaydi va farqi shu remove dan

# 7 Pop() tasodifiy elementni olib tashlaydi xar safar
# mevalar = {"olma", "banan", "gilos"}
# element = mevalar.pop()
# print(element)
# print(mevalar)


# 8 clear() barcha elementlarni o'chiradi
# mevalar = {"olma", "banan", "gilos"}
# mevalar.clear()
# print(mevalar)

# 9 copy() set nusxasini qaytaradi
# mevalar = {"olma", "banan"}
# yangi = mevalar.copy()
# print(yangi)


# 10 union() - ikkita set ni birlashtirish
# A = {"olma", "gilos"}
# B = {"banan", "gilos"}
# yigindi = A.union(B)
# print(yigindi)


# 🔹 11. update() (yana) – birlashtirib o‘zgaruvchiga saqlash
# A = {"olma", "banan"}
# B = {"gilos", "anor"}
# A.update(B)
# print(A)


# 🔹 12. intersection() – umumiy elementlarni olish
# A = {"olma", "banan", "gilos"}
# B = {"banan", "anor", "gilos","olma"}
# C = A.intersection(B)
# print(C)


# 13. intersection_update() – faqat umumiy elementlarni qoldiradi
# A = {"olma", "banan", "gilos","anor"}
# B = {"banan", "anor", "gilos"}
# A.intersection_update(B)
# print(A)


# 🔹 14. difference() – faqat birinchida borlarini oladi
A = {"olma", "banan", "gilos","uzum"}
B = {"banan", "anor"}
print(A.difference(B))


# 🔹 15. difference_update() – farqni o‘zida saqlaydi
# A = {"olma", "banan", "gilos"}
# B = {"banan", "anor"}
# A.difference_update(B)
# print(A)


# 🔹 16. symmetric_difference() – ikkita setdagi farqli elementlarni oladi
# A = {"olma", "banan", "gilos","uzum","anjir"}
# B = {"banan", "anor","shaftoli","anjir"}
# C = A.symmetric_difference(B)
# print(C)

# 17. symmetric_difference_update() – farqli elementlarni saqlaydi
# a = {"olma", "anor","banan"}
# b = {"banan", "uzum","shaftoli"}
# a.symmetric_difference_update(b)
# print(a)

 
# 🔹 18. issubset() – kichik to‘plamligini tekshiradi
# a = {"olma","anor"}     #a set kichik subset ekanligini tekshirmoqda
# b = {"olma","anor","banan"}
# c = a.issubset(b)
# print(c)

# 🔹 19. issuperset() – katta to‘plamligini tekshiradi

# A = {"olma", "banan", "gilos"}  #A ni katta set ekanligini tekshiryapmiz
# B = {"olma", "banan"}
# print(A.issuperset(B))


# 🔹 20. isdisjoint() – umuman umumiy element yo‘qligini tekshiradi
# a = {"olma","anor"}
# b = {"banan","uzum"}
# c = a.isdisjoint(b)
# print(c)


# 🔹 21. in operatori – mavjudligini tekshirish
# mevalar = {"olma", "banan", "gilos"}
# print("anor" not in mevalar)

# 22. setni ro'yhatga ya'ni listga o'zgartirish
# mevalar = {"olma", "banan", "gilos"}
# royxat = list(mevalar)
# print(royxat)
