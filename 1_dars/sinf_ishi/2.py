import random

# raqam = int(input("Raqamni taxmin qil: "))
# a = random.randint(1,1000)
# print(a)
# print(raqam)

# raqam = int(input("Raqamni: "))
# a = chr(random.randint(1,1000))
# b = ord(a)
# print(b)


# ism = "Jasur"
# teskari = ism[::-1]
# print(teskari)

from faker import Faker

# Faker obyektini yaratamiz
fake = Faker()

# Ma'lumotlarni generatsiya qilish
print(f"Ism: {fake.name()}")
print(f"Manzil: {fake.address()}")
print(f"Email: {fake.email()}")
print(f"Matn: {fake.sentence()}")
print(f"SSN: {fake.ssn()}")
print(f"Job: {fake.job()}")