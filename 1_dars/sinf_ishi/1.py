# yil = int(input("Yil kiriting: "))
# print(2026 - yil)

# # 2_masala
# soat = int(input("Soat kiriting: "))
# a = soat * 3600
# print(f"{soat} soat {a} soniya")

# 4_masala
# son = input("Son kiriting: ")
# a = son[::-1]
# print(a)

# 5_masala
# login = (input("Login: "))
# summa = ord(login[0]) + ord(login[1]) + ord(login[2]) 
# print(f"{login}{summa}")

# soat = int(input("Soat: "))
# daqiqa = int(input("Daqiqa: "))
# natija = soat * 60 + daqiqa
# print(f"Film davomimligi: {natija} daqiqa")

# 7_masala
matn = "Python"
a = matn[::-1]
print(a)

# id = (input("Id kiriting: "))
# b = int(id[:2])
# if b <=26:
#     togilgan_yil = 2000+b
# else: 
#     togilgan_yil = 1900 + b

# natija = 2026 - togilgan_yil
# print(f"Yosh: {natija}")

# 9_masala
# belgi = input("Belgi kiriting: ")
# belgi2 = input("Belgi2 kiriting: ")
# print(f"{belgi}{belgi2}")

# 10_masala
# matn = input("Matn kiriting: ")
# matn2 = input("Matn2 kiriting: ")
# a = ("".join([matn,matn2]))
# b = len(a)
# print(f"{a}({b} belgi)")
# print(" ".join(["Salom","dunyo"])) # "Salom dunyo"


# 11_masala
# a = "A"
# b = "b"
# c = "!"
# natija = ord(a) + ord(b) + ord(c)
# print(f"Kodlar yig'indisi: {natija}")

# 12_masala
# a = "a"
# c = (ord(a ) + 2)
# b = chr(c)
# print(b)

# 13_masala
import random
# a = chr(random.randint(97,122))
# f = input("Harf kiriting: ")
# print(f"Sizning harifingiz: {f}")
# print(f"Komputer harfi: {a}")


# 14_masala
# ism = input("Ism kiriting: ")
# a = len(ism)
# b = ord(ism[0])
# c = ord(ism[-1])
# natija = b + c + a
# print(f"Kod: {natija}")

# 15_masala
# a = (random.randint(100,999))
# f = int(input("Son kiriting: "))
# print(f"Sizning soningiz: {f}")
# print(f"Komputer soni: {a}")

# 16_masala
# son = int(input("Son kiriting: "))
# yuzlar = son // 100
# onlar = (son //10) % 10
# birlar  = son % 10
# natija = yuzlar + onlar + birlar
# natija= yuzlar * onlar * birlar
# print("Yigindi: ", natija)
# print("Kopaymtma: ",natija)

# 17_masala
# son = int(input("Son kiriting: "))
# minglar = (son) // 1000%10
# yuzlar = int(son // 100) % 10
# onlar = (son //10) % 10
# birlar  = (son % 10)
# natija = str(f"{birlar}{onlar}{yuzlar}{minglar}")

# print(natija)
# print("Kopaymtma: ",natija)

# 18_masala
# son = input("Son kiriting: ")

# print("O'rtadagi raqam:",son[2])


# 19_masala
# son = int(input("Son kiriting: "))
# onlik  = son // 10 % 10
# birlik = son % 10
# natija = str(f"{birlik}{onlik}")
# print(natija)

# 20_masala
# son = int(input("Son kiriting: "))
# minglar = (son) // 1000%10
# yuzlar = int(son // 100) % 10
# onlar = (son //10) % 10
# birlar  = (son % 10)
# natija = str((f"{minglar}{minglar}{yuzlar}{yuzlar}{onlar}{onlar}{birlar}{birlar}"))
# print(natija)

