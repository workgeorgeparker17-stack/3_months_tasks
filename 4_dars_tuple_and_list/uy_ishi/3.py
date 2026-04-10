# 1 masala
# n = int(input("Necha marta kiritsin: "))
# royhat = []
# for i in range(n):
#     a = int(input("Son kiriting: "))
#     royhat.append(a)
# print(royhat)

# 2 masala
# sonlar = input("Probel bilan son kiriting: ").split(" ")
# royhat = []
# for i in range(len(sonlar)):   
#     sonlar[i] = int(sonlar[i])
# print(len(sonlar))
# print(sonlar[-1])
# print(sonlar[::-1])

# # 3 masala
# royhat = [1,5,0,3,2]
# son = int(input("Qidiriladigan son: "))
# for i in royhat:
#     if son==i:
#         print("Bor")
#         break
# else:
#     print("Yuq")

# 4 masala
# lst = [1,4,1,6,21,5]
# for i in lst:
#     if len(lst)<2:
#         break
#     a = lst.pop(0)
#     b = lst.pop()
#     lst.sort()
#     print(lst)

# 6 masala
# lst = [1,3,5,2,7,4]
# son = int(input("Son kiriting: "))
# for i in lst:
#     if son>i:
#         print(i)

# 7 masala 
# import random
# for i in range(20):
#     a = random.randint(1,100)
#     print(a,end=" ")

# 8 masala
# royhat = [56, 99, 3, 71, 49, 17, 29, 50, 85, 12, 23, 87, 3, 65, 25, 43, 66, 72, 83, 96]
# print(sum(royhat) / len(royhat))

# royhat = [95, 50, 36, 4, 67, 97, 8, 80, 85, 3, 92, 14, 19, 54, 38, 80, 2, 18, 30, 93]
# print(max(royhat),end=" ")
# print(min(royhat),end=" ")

# 11 masala
# royhat = [2, 5, 8, 11, 14]
# count = 0
# for i in royhat:
#     if i % 2 == 0:
#         count+=1
# print(count)

# 12 masala
# royhat = [8,9,10]
# royhat2 = [4,5,6]
# a = 17
# for i in royhat:
#     royhat[1] = a
# royhat.extend(royhat2)
# royhat.pop(0)
# royhat.sort() 

# print(royhat)


# royhat = [8,9,10]
# for i in range(len(royhat)):

#     royhat[i] = royhat[i] * 2
# print(royhat)

# royhat = [1,3,5]
# yangi_royhat = []
# for i in royhat:
# #     yangi_royhat.append(i*2)
# # print(yangi_royhat)

# royhat = [1,3,5]
# # for i in royhat:
# royhat.insert(3,23)
# print(royhat)


# 13 masala


# lst = []

# while True:
#     son = int(input("Son kiriting: "))
#     if son == 0:
#         break
#     if son >10:
#         son = 10
#     lst.append(son)
# print(lst)




# 13 masala
# sozlar = input("Gap: ").split(" ")
# sozlar = [soz[1::] for soz in sozlar]
# print(sozlar)

# 14 masala
# royhat = []
# for i in range(1,51,1):
#     royhat.append(i**2)
# print(royhat)

# sonlar = [chr(son)*(son-ord('a')+1) for son in range(ord('a'), ord('z')+1)]
# print(sonlar)


# 15 masala
# sonlar = []
# for son in range(ord('a'),ord('z')+1):
#     sonlar.append(chr(son)*(son-ord('a')+1))
# print(sonlar)

# 16 masala
# royhat = [3,1,4]
# royhat2 = [3,2,3]
# royhat3 = []
# for i in range(len(royhat)):
#     royhat3.append(royhat[i] + royhat2[i])
# print(royhat3)

# 17 masala
# son = int(input("Son kiriting: "))
# lst = []
# for i in range(1,son+1,1):
#     lst.append(i)
# print(lst)

# royhat = [3,4,5,6]
# x = royhat.pop(-1)
# royhat.insert(0,x)
# print(royhat)


# royhat = [3,4,5,6]
# oxirgi = royhat[-1:]

# boshidan_oxirigacha = royhat[:-1]
# natija = oxirgi + boshidan_oxirigacha
# print(natija)

# royhat = [True, "Salom", 5, 5.6]
# for i in royhat:
#     print(type(i),end=" ")

# royhat = [7, 8, 1, 3, 4, 6, 7, 5]
# yangi_royhat = []
# for i in range(len(royhat)):
#     if i % 2 == 0:
#         yangi_royhat.append(royhat[i]**2)
#     else:
#         yangi_royhat.append(royhat[i]**3)
# print(yangi_royhat)












# lst = [1,2,3,4,5,6]
# new_lst = []
# for i,x in enumerate(lst):
#     if i % 2 ==0:
#         new_lst.append(lst[i]**2)
#     else:
#         new_lst.append(lst[i]**3)
# print(new_lst)
