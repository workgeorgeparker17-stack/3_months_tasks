# son = int(input("Son: "))
# y = 0
# for i in range(1,son):
#     if son % i == 0:
#         y+=i
# if y == son:
#     print("Mukammal")
# else:
#     print("Mukammal emas")


# Bool 
# 1 masala
# son = int(input("Son kiriting: "))
# if son % 3 == 0:
#     print(True)
# else:
#     print(False)

# 3 masala
# son = int(input("Son kiriting: "))
# if son // 10:
#     print(True)
# else:
#     print(False)

# 4_masala
# son = int(input("Son kiriting: "))
# if son > 300 and son % 3 == 0:
#     print(True)
# else:
#     print(False)

# 5_masala
# son = int(input("Son kiriting: "))
# if son >=15 and son <=20:
#     print(True)
# else:
#     print(False)

# # 6_masala
# son = int(input("Son kiriting: "))
# if son >=100 and son <=999:
#     bir = son % 10
#     yuz = son // 100
#     natija = (yuz % 2 != 0 and bir % 2 == 0)
#     print(natija)
# else:
#     print("Xato")      

# son = int(input("Son kiriting: "))
# if son >=100 and son <=999:
#     yangi_son = son - 1
#     oxirgi_son = yangi_son % 10
#     if (oxirgi_son % 2 !=0):
#         print(True)
#     else:
#         print(False)

# son = int(input("Son: "))
# if son >=100 and son<=999:
#     yuz = son //100
#     on = son // 10 % 10
#     bir = son % 10
#     if bir !=0:
#         print(True)
#     else:
#         print(False)



# Orta masalalar bool
# 1_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# c = int(input("Son3: "))

# if a<b<c:
#     print(True)
# else:
#     print(False)

# 2_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# if a % 2 !=0 and b % 2 !=0:
#     print(True)
# else:
#     print(False)

# 3_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# if a % 2 !=0 or b % 2 !=0:
#     print(True)
# else:
#     print(False)

# 4_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# if a % 2 !=0 and b % 2 ==0 or a % 2 ==0 and b % 2 !=0 :
#     print(True)
# else:
#     print(False)

# 5_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# if a % 2 !=0 and b % 2 !=0 or a % 2 ==0 and b % 2 ==0 :
#     print(True)
# else:
#     print(False)

# 6_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# c = int(input("Son3: "))
# if a > 0 and b > 0 and c > 0:
#     print(True)
# else:
#     print(False)

# 7_masala
# a = int(input("Son: "))
# b = int(input("Son2: "))
# c = int(input("Son3: "))
# if a > 0 or b > 0 or c > 0:
#     print(True)
# else:
#     print(False)

# 9_masala
# a = int(input("Son: "))
# if a >=10 and a<=99 and a % 2 ==0:
#     print(True)
# else:
#     print(False)

# 10_masala
# a = int(input("Son: "))
# b = int(input("Son: "))
# c = int(input("Son: "))

# if a == b or b == c or c == a:
#     print(True)
# else:
#     print(False)

# 11_masala
# a = int(input("Son: "))
# b = int(input("Son: "))
# c = int(input("Son: "))
# if (a<0 and b < 0 and c > 0 or b >0 and c < 0 and a < 0 or a>0 and b<0 and c<0):
#     print(True)
# else:
#     print(False)

# 12_masala
# a = int(input("Son: "))
# b = int(input("Son: "))
# c = int(input("Son: "))
# if a !=b and b !=c and c !=a:
#     print(True)
# else:
#     print(False)

# 13_masala
# a = int(input("Son: "))
# b = int(input("Son: "))
# c = int(input("Son: "))
# if a>b>c or a<b<c:
#     print(True)
# else:
#     print(False)

# 14_masala

# x = int(input("X: "))
# y = int(input("Y: "))
# if x==y:
#     print(True)
# else:
#     print(False)

# if lik masalalar
# 1

# son = int(input("Son: "))
# if son % 2 == 0:
#     print("Juft")
# else:
#     print("Toq")

# 2

# kun = int(input("Kun: "))
# if kun == 1:
#     print("Dushanba")
# elif kun == 2:
#     print("Seshanba")
# elif kun == 3:
#     print("Chorshanba")
# elif kun == 4:
#     print("Payshanba")
# elif kun == 5:
#     print("Juma")
# elif kun == 6:
#     print("Shanba")
# elif kun == 7:
#     print("Yakshanba")
# else:
#     print("Bunday kun yo'q")

# 3

# baho = int(input("Baho: "))
# if baho >=80 and baho <=100:
#     print("5")
# elif baho >=60 and baho <=79:
#     print("4")
# elif baho >=40 and baho <=59:
#     print("3")
# elif baho >=20 and baho <=39:
#     print("2")
# elif baho >=0 and baho <=19:
#     print("1")
# else:
#     print("Siz bebahosiz")

# 4

# x = int(input("X="))
# y = int(input("Y="))
# if x > 0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y <0:
#     print("4")


# 5 

# son = int(input("Son: "))
# if son % 3 == 0 and son % 5 !=0:
#     print("Fizz")
# elif son % 5 == 0 and son % 3 !=0:
#     print("Buzz")
# elif son % 3 == 0 and son % 5 == 0:
#     print("FizzBuzz")

# if ortalari
# 1

# a = int(input("Son: "))
# if a >=10 and a <=99:
#     natija = a // 10 % 10
#     natija1 = a % 10
# if(natija < natija1):
#     print(natija)
# else:
#     print(natija1)

# 2
# u1 = int(input("U1="))
# u2 = int(input("U2="))
# u3 = int(input("U3="))

# if u1 + u2 == u3 or u2 + u3 == u1 or u3 + u1 == u2:
#     print("Bunday uchburchak mavjud")
# else:
#     print("Bunday uchburchak mavjud emas!")

# 3
# harf = input("Harf kiriting: ").lower()
# unlilar = "auoei"
# undoshlar = "bcdfghjklmnpqrstvwxyz"

# if harf.isalpha and harf in undoshlar:
#     print("undosh")
# elif harf in unlilar:
#     print("unli")
# elif harf not in undoshlar and harf not in unlilar:
#     print("Bunday harf yo'q")




# harf = input("Harf=").upper()
# harf2 = input("Harf2=").upper()
# if harf == harf2:
#     print(True)
# else:
#     print(False)



# harf = input("Harf=")

# if harf.isalpha():
#     a = harf.upper()
    # print(a)

# oy = int(input("Oy raqamini kiriting: "))

# if oy == 1 or oy == 2 or oy == 12:
#     print("Qish")
# elif oy == 3 or oy == 4 or oy == 5:
#     print("Bahor")
# elif oy == 6 or oy == 7 or oy == 8:
#     print("Yoz")
# elif oy == 9 or oy == 10 or oy ==11:
#     print("Kuz")
# else:
#     print("Bunday oy yo'q")


# oy = int(input("Oy raqamini kiriting: "))

# if oy == 1 or oy == 3 or oy == 5 or oy == 7 or oy == 8 or oy == 10 or oy == 12:
#     print(31)
# elif oy == 4 or oy == 5 or oy == 9 or oy == 11:
#     print(30)
# elif oy == 2:
#     print(28)



# son = int(input("Son="))
# if son >=1 and son <=1999:
#     if 1<=son <=9:
#         xona = "bir xonali"
#     elif 10 <=son <=99:
#         xona = "ikki xonali"
#     elif 100<=son <=999:
#         xona = "uch xonali"
#     else:
#         xona = "to'rt xonali"
#     if son % 2 == 0:
#         turi = "juft"
#     else:
#         turi = "toq"
#     print(f"{xona} {turi}")


# son = int(input("Son="))

# birlar = ["","bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "toqqiz"]
# onlar = ["","on", "yigirma", "ottiz", "qirq","ellik", "oltmish", "yetmish", "sakson","to'qson"]
# if 100<=son <=999:
#     yuz_xona = son // 100 
#     on_xona = (son % 100) //10
#     bir_xona = son % 10
    
#     natija = f"{birlar[yuz_xona]} yuz {onlar[on_xona]} {birlar[bir_xona]}"
#     print(natija)
        

# for and while 
# son = 1000
# for i in range(100,son):
#     bir = i % 10
#     on = (i // 10) % 10
#     yuz = (i // 100)

#     if(bir == on or on == yuz or yuz == bir):
#         print(i)


# for i in range(100,1000): 
#     s = str(i)
#     if s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
#         print(i)


# for i in range(1,501,1):
#     print(i)

# for i in range(250,-1,-1):
#     print(i)

# for i in range(530,9,-2):
#     print(i)

# son = int(input("Son="))
# y = 0
# for i in range(1,son+1,1):
#     bir = i % 10
#     on = i // 10 % 10
#     yuz = i // 100 % 10
#     y = bir + on + yuz
# print(y)

# son = int(input("Son="))
# y = 0
# for i in range(1,son):
#     if son % i == 0:
#         y+=i
# if y == son:
#     print("Mukammal")
# else:
#     print("Mukammal emas")

# n = int(input("N="))
# y = 0
# for i in range(1,n):
#     if i % 2 == 0:
#         y+=i
# print(y)
  

# for i in range(97,123):
#     print(chr(i))


# y = 0
# for i in range(1,501):
#     if i % 2 != 0:
#         y+=i
# str_y = str(y)
# if str_y == str_y[::-1]:
#     print(True)
# else:
#     print(False)

# y = 0
# n = int(input("N="))
# m = int(input("M="))
# k = int(input("K="))
# for i in range(n,m,k):
#     if i % 2 == 0:
#         y+=i
# print(y)


# y = 0
# count = 0
# n = int(input("N="))
# m = int(input("M="))
# k = int(input("K="))
# for i in range(n,m+1):
#     if i % 2 == 0:
#         y+=i
#         count+=1

#     if count == k:
#         break
# print(y)

# son = (input("Son>>"))
# son_teskari = son[::-1]
# natija = int(son) - int(son_teskari)
# print(f"Farq {natija}")

# n = int(input("N="))
# a=0
# b=1
# temp =0
# for i in range(n):
#     print(a,end=" ")
#     temp = a
#     a = b+a
#     b = temp
    
  
# 6 masala
# son = int(input("Son="))
# for i in range(1,son+1):
#     if son % i == 0:
#         print(i,end=" ")


# 7 masala
# a = int(input("Son="))
# b = int(input("Son2="))
# for i in range(a,b+1):
#     if i % 2 == 0:
#         print(i * -1)
#     else:
#         print(i)

# 8 masala

# son = int(input("Son="))
# son = abs(son)
# xonalar_soni = 0
# if son == 0:
#     xonalar_soni = 1
# else:

#     while son !=0:
#         son = son // 10
#         xonalar_soni = xonalar_soni +1
# print(xonalar_soni)


# for i in range(100,1000):
#     s = str(i)
#     if "3" in s:
#         print(i)


# for i in range(100,1000):
#     s = str(i)
#     if s[0] == "3" or s[1] == "3" or s[2] == "3":
#         print(i)

# son = input("Son=")
# if son[0] == son[1] or son[1] == son[2] or son[2] == son[3] or son[3] == son[4]:
#     print("Bor")
# else:
#     print("Yoq")


# n = int(input("N="))
# if n == 0 or n < 0:
#     print("Xato")
# k = 1
# while k * k<=n:
#     k+=1
# print(k)

# n = int(input("N="))
# if n >=1:
    
#     k = 0
#     daraja = 1
#     while daraja*3<=n:
#         daraja *=3
#         k+=1
# print(k)

# n = int(input("N="))
# max = 0
# while n !=0:
#     a = n % 10
#     n //=10
#     if a > max:
#         max = a
# print(max)


# n = int(input("N="))
# for i in range(1,n+1,1):
#     print(i, end=" ")
# for i in range(n-1,0,-1):
#     print(i, end=" ")

    

# n = int(input("N="))
# n_nusxa = n
# yigindi = 0
# while n!=0:
#     yigindi +=n % 10
#     n //=10
# n_nusxa %= yigindi
# print(yigindi)
# print(n_nusxa)

# a = int(input("A="))
# b = int(input("B="))
# y = 0
# for i in range(a,b+1,1):
#     y+=i
# print(y)


# n = int(input("N="))
# faktorial = 1
# for i in range(1,n+1,1):
#     faktorial *= i
# print(faktorial)

# son = int(input("Son="))
# count = 0
# while son > 0 and son% 2 == 0:
#     son = son // 2 
#     count+=1
    

# print(count)

# a = int(input("son="))
# for i in range(a,a*2+1,1):
#     print(i)


# a = int(input("Son="))
# b = int(input("Son2="))
# tubmi = 0
# for i in range(a,b):
#     if i < 2:
#         continue
#     tubmi = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             tubmi = False
#             break
#     if tubmi == True:
#         print(i)


# n = int(input("N="))
# for i in range(1,n,1):
#     if n % i == 0 and i % 2 !=0:
#         print(i)

# n = int(input("N="))
# y = 0
# for i in range(1,n,1):
#     if n % i == 0:
#         y+=i
# print(y)

# n = int(input("N="))
# m = int(input("M="))
# tubmi = 0
# y = 0
# for i in range(n,m):
#     if i < 2:
#         continue
#     tubmi = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             tubmi = False
#             break
#     if tubmi == True:
#         y+=i
# print(y)


# n = 10
# for i in range(0,n):
#     for j in range(0,n):
#         if i == n-1 or i == 0 or j == n-1 or j == 0 or i == j or i + j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")          
#     print()


# uyga vazifa for and while 

# 1
# n = int(input("N="))
# y = 0
# for i in range(1,n+1,1):
#     if i % 2 !=0:
#         y +=i
# print(y)

# 2
# n = int(input("N="))
# faktorial = 1
# for i in range(1,n+1,1):
#     faktorial *=i
# print(faktorial)

# 3 
# a = int(input("A="))
# b = int(input("B="))
# juft_y = 0
# for i in range(a,b+1,1):
#     if i % 2 == 0:
#         juft_y+=i

# print(juft_y)

# 4 

# son = int(input("Son="))
# while son !=0:
#     n = son % 10
#     son //=10
#     print(n,end="")

# 6
# n = int(input("N="))
# tubmi = 0
# for i in range(1,n):
#     if i < 2:
#         continue
#     tubmi = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             tubmi = False
#     if tubmi == True:
#         print(i)

# 7
# son = int(input("Son="))
# y = 0
# while son !=0:
#     n = son % 10
#     son //=10
#     y+=n
# print(y)

# 8
# son = int(input("Son="))
# y = 0
# while son !=0:
#     n = son % 10
#     son //=10
#     y+=n*n
# print(y)


# son = int(input("Son="))
# count = 0
# for i in range(100,son,1):
#     a = str(son)
# if a[0] == a[3]:
#     print(True)
# else:
#     print(False)


y = 0
for i in range(1,501):
    if i % 2 != 0:
        y += i

y = str(y)
if y == y[::-1]:
    print("Palindrom")
else:
    print("Palindrom emas")
