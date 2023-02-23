# masalalr ishlash
# 1-masala
# son=int(input('sonni kiriting'))
# xaftakunlar={
#     0:"Yakshanba",1:'Dushanba',2:"Seshanba",3:"Chorshanba",4:"Payshanba",5:"Juma",6:"Shanba"
# }
# if(0<=son<=365):
#     kun=son%7
#     print(xaftakunlar[kun])

# else:
#     print('0-365 orasida son bering !')

# 2-masala
# -masala
#4-masala



#5-masala
# son=int(input('sonni kiriting'))
# xaftakunlar={
#     1:'Dushanba',2:"Seshanba",3:"Chorshanba",4:"Payshanba",5:"Juma",6:"Shanba",7:'yakshanba'
# }
# if(1<=son<=365):
#     kun=son%7
#     print(xaftakunlar[kun])

# else:
#     print('0-365 orasida son bering !')

# 6-masala
#  


















# son=int(input('sonni kiritnibg: '))
# teskari=0
# yigindi=0
# while son>0:
#     teskari=teskari*10+son%10
#     yigindi+=son%10
#     son//=10
#     print(teskari,yigindi)

# talaba={
#     "ism":"Anna",
#     "yosh":23,
#     "isMarried":True,
#     " hobbies":["listening to music , playing a computer games"],
#     "salary":2800,
# }





# talaba.pop('ism')
# talaba.popitem()
# del talaba["yosh"]
# del talaba
# print(talaba)

# print(talaba['yosh'])
# print(talaba.get('yosh1','Ushbu keywords mavjud emas'))





# print('yosh1'in talaba.keys())
# print(talaba.items())

# for key,val in talaba.items():
#     print(f'{key}:{val}')



# talaba={
#     "ism":"Anna",
#     "yosh":23,
#     "isMarried":True,
#     " hobbies":["listening to music , playing a computer games"],
#     "salary":2800,
# }
# key=int(input('keyni kiriting: '))
# if key in talaba:
#     print(f'{key} - {talaba[key]} mavjud...')
# else:
#     print(f'{key} - ushbu key mavjud emas ...')




# colorlist=['balck','white','gren','white','red','gren','yellow']

# colorset={'balck','white','gren','white','red','gren','yellow'}

# colorset2=colorset.copy()
# print(colorset)
# numbers={1,2,3,4,5,6,7,8,9,10}
# print(colorlist)
# print()
# print(colorlist,type(colorlist))

# colorset.add('indigo')
# print(colorlist)
# sortlist=list(set(colorlist))
# print(sortlist)

# numbers.pop()
# print(numbers)


# st={"Android","fullStack","Cotlin","sass"}
# lang={"html","sass","fullsatack"}
# un=st.union(lang)
# un2=st | lang
# print(un)
# print(un2)


# inter=st.intersection(lang)
# inter2=st & lang
# print(inter)
# print(inter2)


# dif=st.intersection(lang)
# dif2=st & lang
# print(dif)
# print(dif2)

# func keirsh















# print(talaba,type(talaba))

# print(talaba.keys())
# print(talaba.values())

# talaba1=talaba.copy()
# c=0;
# for i in talaba.keys():
#     print(f'{c} => {i}')
#     c+=1








# function KIRISH

# def salomalsh(ism,familya,yosh):
#     print(f'{ism},{familya},{yosh}')
  

# salomalsh(ism='abdullo',familya='hakimov',yosh=22)

# def calc(a,b,c):
#     natija=a+b+c
#     return natija
# a=int(input('a: '))
# b=int(input('b: '))
# c=int(input('c: '))
# natija=calc(a,b,c)
# print(natija)

