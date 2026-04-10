# 2 masala

# son = input("Probel bilan son kiriting: ").split(" ")
# lst = []
# for i in range(len(son)):
#     son[i] = int(son[i])
# print("Umumiy soni",len(son))
# print("Oxirigi elementi", son[-1])
# print("Teskari", son[::-1])


# 1 masala
# n = int(input("N="))
# lst = []
# for i in range(n):
#     a = int(input("Son kiriting: "))
#     lst.append(a)
# print(lst) 

# 3 masala

# sonlar = [1,3,4,5,2]
# if 6 in sonlar:
#     print("Bor")
# else:
#     print("Yoq")


# 3 masala
# sonlar = [1,3,4,5,2]
# son = int(input("Son kiriting: "))
# for i in sonlar:
#     if son == i:
#         print("Bor")
#         break
# else:
#     print("Yoq")
        

# 5 masala
# sonlar = [3, 5, 6, 34, 78, 33, 23]

# for i in sonlar:
#     a = sonlar.pop(0)
# print(a)


# 7 masala
# import random
# lst = []
# for i in range(20):
#     lst.append(random.randint(1,101))
# print(lst)

# 8 masala

# royhat = [56, 99, 3, 71, 49, 17, 29, 50, 85, 12, 23, 87, 3, 65, 25, 43, 66, 72, 83, 96]
# print("Ortachasi", sum(royhat) / len(royhat))


# masala
# lst = [2, 5, 8, 11, 14]
# lst = [10 if lst[i] > 10 else lst[i] for i in range(len(lst))]
# print(lst)

# sonlar = [3, -4, 0, 0, -6, 2, 0]
# manfiy = [son for son in sonlar if son <0]
# musbat = [son for son in sonlar if son >0]

# sonlar1 = [son for son in sonlar if son != 0]
# nollar = [son for son in sonlar if son == 0]

# print(manfiy + musbat)

# sonlar = [1,2,30,4,5]
# harf = 'e'
# for i in sonlar:

#     a = f"{harf}{i}"
#     print(a, end=" ") 