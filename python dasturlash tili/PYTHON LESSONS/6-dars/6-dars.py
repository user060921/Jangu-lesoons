
# 20-masala
# a=int(input('son kiriting'))
# yuzlik=a//100#4
# qoldik=a%100
# onlik=qoldik//10#4
# birlik=qoldik%10#3
# result1=yuzlik!=onlik!=birlik
# print(result1)

# # 20-masala
# a=int(input('son kiriting'))
# yuzlik=a//100#4
# qoldik=a%100
# onlik=qoldik//10#4
# birlik=qoldik%10#3
# result1=(yuzlik!=onlik and onlik!=birlik) and  (yuzlik!=birlik and onlik!=birlik)
# print(result1)

# # 21-masala
# a=int(input('son kiriting'))
# yuzlik=a//100#4
# qoldik=a%100
# onlik=qoldik//10#4
# birlik=qoldik%10#3
# result1=yuzlik<=onlik<=birlik or birlik<=onlik<=yuzlik
# print(result1)

# 23-masala
# a=int(input('son kiriting'))
# yuzlik=a//100#4
# qoldik=a%100
# onlik=qoldik//10#4
# birlik=qoldik%10#3
# result1=yuzlik==birlik
# print(result1)

# 24-masala
# a=int(input('son kiriting'))
# b=int(input('son kiriting'))
# c=int(input('son kiriting'))
# d=b*b-4*a*c
# natija=d>=0
# print(natija)

# # 25-masala
# x=int(input('son kiriting'))
# y=int(input('son kiriting'))
# chorak=x<0 and y>0
# print(chorak)

# 26-masala
# x=int(input('son kiriting'))
# y=int(input('son kiriting'))
# chorak=y<0 and x>0
# print(chorak)

# 27-masala
# x=int(input('son kiriting'))
# y=int(input('son kiriting'))
# chorak=(x<0 and y>0) or( x<0 and y<0)
# print(chorak)

# 28-masala
# x=int(input('son kiriting'))
# y=int(input('son kiriting'))
# chorak=(x>0 and y>0) or( x<0 and y<0)
# print(chorak)

# # 30-masala
# a=int(input('son kiriting'))
# b=int(input('son kiriting'))
# c=int(input('son kiriting'))
# result1=a==b==c
# print(result1)

# 31-masala
# a=int(input('son kiriting'))
# b=int(input('son kiriting'))
# c=int(input('son kiriting'))
# result1=a==c
# print(result1)

# import random

# print(random.random()*100)
# print(random.randrange(1,25,4))
# print(random.randint(1,5))
# colors=['black','white','brown','dark','yellow','orange','qongiz']
# tasodif=random.choice(colors)
# random.shuffle(colors)
# print(colors)
# print(random.choices(colors,k=3))
# txt='I love Python'
# print(random.choice(txt))
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2008,5))