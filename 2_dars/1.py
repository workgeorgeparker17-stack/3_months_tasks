# a = int(input("son="))
# b = int(input("son="))
# print(a % 2 == 0 and b % 2 !=0 or a % 2 !=0 and b % 2 == 0)

# 2_masala
# kun = int(input("Kun kiriting: "))
# if(kun == 1):
#     print("Dushanba")
# elif(kun == 2):
#     print("Seshanba")
# elif(kun == 3):
#     print("Chorshanba")
# elif(kun == 4):
#     print("Payshanba")
# elif(kun == 5):
#     print("Juma")
# elif(kun == 6):
#     print("Shanba")
# elif(kun == 7):
#     print("Yakshanba")
# else:
#     print("Bunday kun yo'q")

# 3_masala
# baho = int(input("Baho kiriting: "))
# if baho >=80 and baho <=100:
#     print("5")
# elif baho >=60 and baho <=79:
#     print("4")
# elif baho >=40 and baho <=59:
#     print("3")
# elif baho >=20 and baho <=39:
#     print("2")
# elif baho >=0 and baho <=19:
#     print("2")
# else:
#     print("Siz bebahosiz")

# 5_masala

# son = int(input("Son kiriting: "))
# if(son % 3 == 0 and son % 5 !=0):
#     print("Fizz")
# elif(son % 5 == 0 and son % 3 !=0):
#     print("Buzz")
# elif(son % 5 == 0 and son % 3 ==0):
#     print("FizzBuzz")


# x = int(input("X="))
# y = int(input("Y="))
# if x>0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y < 0:
#     print("4")


# ORTA
# son = input("Son=")
# if son[0] < son[1]:
#     print(son[0]) 
# else:
#     print(son[1])   


# u1 = int(input("U1="))
# u2 = int(input("U2="))
# u3 = int(input("U3="))

# if u1+u2==u3:
#     print("Bunday uchburchak mavjud!")
# elif u1+u3==u2:
#     print("Bunday uchburchak mavjud!")
# elif u2+u3==u1:
#     print("Bunday uchburchak mavjud!")
# elif u1+u3!=u2:
#     print("Bunday uchburchak mavjud emas!")
# elif u2+u3!=u1:
#     print("Bunday uchburchak mavjud emas!")
# elif u1+u2!=u3:
#     print("Bunday uchburchak mavjud emas!")



# mukammal raqam
son = int(input("Son kiriting: "))
y = 0
for i in range(1,son):
    if son % i == 0:
        y+=i
if y == son:
    print("Mukammal son")
else:
    print("Mukammal emas")