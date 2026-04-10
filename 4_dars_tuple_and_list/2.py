# sonlar = (input("Probel bilan kiriting: ")).split(" ")

# for i in range(len(sonlar)):
#     sonlar[i] = int(sonlar[i])    
# sonlar = [3, 5, 6, 34, 78, 33,23]
# raqam = 3
# for son in sonlar:
#     a = son
#     while son!=0:
#         if son % 10!=raqam:
#             break
#         son //=10
#     else:
#         print(a)


# Uyga vazifa 
# 1 masala
# lst = [1, 2, 33, 5, 6, 7, 7]
# son = (input("Son kiriting: "))

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] + lst[j] == int(son):
#             print(f"Indekslar {i}, {j}")

# 2 masala
# lst = [1,4,6,8]
# yangi_lst = []
# for i in range(len(lst)):
#     yangi_lst.append(lst[i] * 2)
# print(yangi_lst)

# my_tuple = (10, 20, 30, 40)
# print(my_tuple.index(20))  # Natija: 1
# 3 masala
# lst = (10, 20, 40), (40, 50, 60), (70, 80, 90)
# yangi_lst = [t[:-1] + (100,) for t in lst]
# print(yangi_lst)

# 4 masala
# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# yangi_lst = []
# for i in lst:
#     if i:
#         yangi_lst.append(i)
# print(yangi_lst)


# 5 masala
# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# lst.sort(key=lambda x: float(x[1]), reverse=True)
# print(lst)

# 6 masala
# matn = input("Matn kiriting: ")
# for i in matn:
#     tple = tuple(matn)
# print(tple)

# 7 masala
# lst = [1, 2, 3, 4]
# prefix = 'emp'
# for i in lst:
#     s = [f"{prefix}{i}"]
#     print(s,end="")

# 8 masala
# matn = "Salom aziz qalaysan".split(" ")
# n = len(matn)
# for i in range(len(matn)):
#     for j in range(0,n-i-1):
#         if len(matn[j])>len(matn[j+1]):
#             matn[j],matn[j+1] = matn[j+1], matn[j]
# print(matn)

# 9 masala
# lst = [12,'salom',4.5,'dunyo',True]
# yangi_lst = []
# a = lst.pop(1)
# b = lst.pop(2)
# yangi_lst.append(b)
# yangi_lst.append(a)
# print(yangi_lst,end=" ")

# 10 masala
# t = (-3, 5, 0, 9, -1, 4)
# musbatlar = []
# for i in range(len(t)):
#     if t[i] > 0:
#         musbatlar.append(t[i])
# print(tuple(musbatlar))

# 11 masala
# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# yangi_matn = []
# yangi_raqam = []
# for i in lst:
#     if type(i) == str:
#         yangi_matn.append([i])
#     elif type(i) == int:
#         yangi_raqam.append([i])

# yangi_matn.sort()
# yangi_raqam.sort(reverse=True)
# print(yangi_matn)
# print(yangi_raqam)

# 12 masala
# lst = [(3, 10), (1, 20), (2, 30)]
# lst.sort(key=lambda i: int(i[0]),reverse=False)
# print(lst)

# 13 masala
# lst = [1, 2, 3, 4]
# yangi_lst = []
# for i in lst:
#     yangi_lst.append(i**2)
# print(yangi_lst)

# 14 masala
# lst = ['salom', 'dunyo', 'python']
# matn = str(lst).title()
# print(matn)

# 15 masala
# tple = (1,2,3,4,5)
# y = 0
# for i in tple:
#     y+=i
# print(y)


# n = 5

# orta 3
# lst = []
# for i in range(n+1):
#     lst.append(1)
#     lst.extend([0]*i)
#     max = 0
# print(lst)
# print(f"Maksimum nollar soni {i} ta")

# orta 4 
# royhat = [1,1,2,3,4,3,0,0]
# yangi_royhat = []
# for i in royhat:
#     if i not in yangi_royhat:
#         yangi_royhat.append(i)
# print(yangi_royhat)

# orta 5 
# royhat = [3, 4, 0, 0, 6, 2, 0]
# yangi_royhat = []
# a = royhat.pop()
# b = royhat.pop(2)
# c = royhat.pop(2)
# royhat.append(a)
# royhat.append(b)
# royhat.append(c)
# print(royhat)

# orta 6
# sonlar = [3, -4, 0, 0, -6, 2, 0]
# sonlar1 = [son for son in sonlar if son != 0]
# nollar = [son for son in sonlar if son == 0]
# sonlar1.extend(nollar)
# print(sonlar1)

# orta 7
# lst = ['p','q']
# n = 5
# natija=[]
# for i in range(1,n+1,1):
#     for char in lst:
#         natija.append(char+str(i))
# print(natija)

# lst = [
#     ["fizika", 88.5, 3],
#     ("Matematika", 95.0, 1),
#     ["fizika", 92.0, 7],
#     ("matematika", 95.0, 4),
#     ["Fizika", 88.5, 1],
#     ("kimyo", 78.0, 2),
#     ["MATEMATIKA", 88.0, 9],
#     ("kimyo", 78.0, 5),
# ]
# for i in range(0, len(lst)-1):
#     for j in range(0, len(lst)-1):
#         if lst[j][0] > lst[j+1][0]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# print(lst)



# lst = [
#     ('Anvar', 'Sherzodov'),
#     ('Ali', 'Karimov'),
#     ('Bekzod', 'Toshmatov'),
#     ('Jasur', 'Rahimov'),
#     ('Sardor', 'Xolmatov'),
#     ('Dilshod', 'Yusupov'),
#     ('Akmal', 'Ergashev'),
#     ('Ulugbek', 'Qodirov'),
#     ('Shahzod', 'Islomov'),
#     ('Miraziz', 'Nazarov')
# ]
# # lst = [13,4,5,6]
# print(lst)
# # lst.sort()
# for i in range(0, len(lst)-1): 
#     for j in range(0, len(lst)-1): 
#         if (lst[j][1]) > (lst[j+1][1]):
#             # a,b=b,a
#             lst[j], lst[j+1] = lst[j+1], lst[j]

# for ism in lst:
#     print(f"{ism[0]:<15} | {ism[1]:<15}")



# lst = [
#     ('Anvar', [3, 4, 5]),
#     ('Ali', [5, 6, 2]),
#     ('Bekzod', [4, 5, 3]),
#     ('Jasur', [5, 5, 4]),
#     ('Sardor', [3, 6, 5]),
#     ('Dilshod', [4, 4, 4]),
#     ('Akmal', [5, 3, 5]),
#     ('Ulugbek', [6, 5, 4]),
#     ('Shahzod', [3, 5, 6]),
#     ('Miraziz', [5, 4, 3])
# ]
# for i in range(0, len(lst)-1): 
#     for j in range(0, len(lst)-1): 
#         if sum(lst[j][1])/len(lst[j][1]) > sum(lst[j+1][1])/len(lst[j+1][1]):
#             # a,b=b,a
#             lst[j], lst[j+1] = lst[j+1], lst[j]

# # for ism in lst:
#     # print(f"{ism[0]:<15} | {ism[1]:<15}")
# # print(lst)
# for ism,ball in lst:
#     print(f"{ism} | {ball}")


lst = [
    ["fizika", 88.5, 3],
    ("Matematika", 95.0, 1),
    ["fizika", 92.0, 7],
    ("matematika", 95.0, 4),
    ["Fizika", 88.5, 1],
    ("kimyo", 78.0, 2),
    ["MATEMATIKA", 88.0, 9],
    ("kimyo", 78.0, 5),
]

for i in range(0, len(lst)-1): 
    for j in range(0, len(lst)-1): 
        if lst[j][0].upper() > lst[j+1][0].upper():
            # a,b=b,a
            lst[j], lst[j+1] = lst[j+1], lst[j]


for ism in lst:
    print(f"{ism}")
