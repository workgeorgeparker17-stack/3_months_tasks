# 1 masala
# set1 = {1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
# yigindi = set1 & set2
# ayirma_farq = set1 - set2
# a = sum(yigindi)
# b = sum(ayirma_farq)
# c = a - b
# print(c)

# 2 masala
# set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
# set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
# set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}
# bir_ikki = set1 & set2 
# natija = bir_ikki.difference(set3)

# print(natija)

# 3 masala
# set1={4,5,6,7,8,9}	
# set2={5,6,7,10,11}
# a = set1 ^ set2
# b = set1 & set2
# yigindi = sum(a)
# u_yigindi = sum(b)
# print(yigindi - u_yigindi)

# 4 masala

# set1={"Artel","Alif","Yandex", "Google", "Meta"}
# set2={"Google", "Apple", "Amazon", "Meta"}
# set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

# umumiy = set1 & set2 & set3
# faqat_ikki_uch = set2 & set3
# faqat_bir = set1 - faqat_ikki_uch 
# print(f"Umumiy elementlar: {umumiy}")
# print(f"Faqat birinchi setda mavjud: {faqat_bir}")

# 5 masala

# set1={2,3,4,5,6}
# set2={4,5,6,7,8,9}
# umumiymas_yigindi = set1 ^ set2
# a = sum(umumiymas_yigindi)
# print(a)

# 6 masala
# set1={100, 20, 45, 80, 70, 50}
# set2={30, 55, 70, 60, 32, 100}
# a = set1 | set2
# numbers = a.copy()

# for son in numbers:
#     if son <= 60:
#         a.remove(son)
# b = a & set2
# c = len(b)
# yigindi = sum(b)
# d = yigindi // c
# print(f"O'rtachasi: {d}")


# 6 masala 2-usul
# set1={100, 20, 45, 80, 70, 50}
# set2={30, 55, 70, 60, 32, 100}

# set1 = {son for son in set1 if son >=60}
# set2 = {son for son in set2 if son >=60}
# a = set1 & set2
# b = len(a)
# c = sum(a)
# d = c //b
# print(d)

# 7 masala
# nums = {1,2,2,1}
# nums2 = {2,2}
# a = nums & nums2
# print(a)

# 8 masala

# nums = {1,2,3}
# nums2 = {2,4,6}
# c = nums ^ nums2
# list1 = list(nums - nums2)
# list2 = list(nums2 - nums)
# natija = [list1,list2]
# print(natija)


# 9 masala 
# from collections import Counter
# nums = [1,2,2,3,3,1,4]
# cnt = Counter(nums)
# mx = max(cnt.values())
# a = sum(x for x in cnt.values() if x == mx)
# print(a)

# ustoz 9 masalani yechimini ai bilan qilganman va tushundim yechimni

# 10 masala

# set1 = {1,2,3,4,1,2}
# a = list(set1)
# print(a)


# 11 masala
# set1 = {2,3,4}
# set2 = {4,5,1}
# c = set1.difference(set2)
# print(c)