son = int(input("Son kiriting: "))
yuzlik = (son //100) % 10
onlik = (son //10)%10
birlik = son % 10
yigindi = yuzlik + onlik + birlik
print(yigindi)