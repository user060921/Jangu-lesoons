# class TALABA:
#     def __init__(self,ism,familya,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#     def introduce(self):
#         return f'Talaba ismi:{self.ism},Familya:{self.familya},yosh:{self.tyil}'

# talaba1=TALABA('Alisher','Ganiyev',1999)
# talaba2=TALABA('Ibroxim','Sadriddinov','2009') 

# print(talaba1.introduce())
# print(talaba2.introduce())


# print(talaba1.ism)
# print(talaba1.familya)
# print(talaba1.tyil)

                # metodlarda ishlangani

# class TALABA:
#     def __init__(self,ism,familya,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#     def get_fullname(self):
#         return f'my fullname is - {self.ism} {self.familya}'

#     def get_age(self):
#         return tyil.self.tyil

# talaba1=TALABA('Alisher','Ganiyev',1999)
# talaba2=TALABA('Ibroxim','Sadriddinov','2009') 

# print(talaba1.get_fullname())
# print(talaba2.get_fullname())




# __________________________________________________________________
# class Gullar:
#     def init(self,nomi,turi,rangi):
#         self.name=nomi
#         self.sname=turi
#         self.date=rangi
#         self.rangi=rangi

#     def introduce(self):
#         return f'Talaba ismi:{self.name},Familya{self.sname},yosh:{self.date}'
#     def get_fullname(self) :
#         return f'name of my flowers are -{self.name}{self.sname}'
#     def get_age(self,year):
#         return year-self.date
# talaba1=Gullar('qorashakhzoda',' Gul',2019)
# talaba2=Gullar('qizil','-Gul',2020)
# talaba3=Gullar('oq','-atirgul',2021)
# talaba4=Gullar('geran','-gul',2022)
# talaba5=Gullar('geran','-gul',2023)

# # print(talaba1.introduce())
# # print(talaba2.introduce())

# # print(talaba1.get_fullname())
# # print(talaba1.get_age(2023))

# # print(talaba2.get_fullname())
# # print(talaba2.get_age(2023))

# # print(talaba3.get_fullname())
# # print(talaba3.get_age(2023))

# print(talaba4.get_fullname())
# print(talaba4.get_age(2023))

# # print(talaba5.get_fullname())
# # print(talaba5.get_age(2023))

# # print(talaba1.name)
# # print(talaba1.sname)
# # print(talaba1.date)
# class Talaba:
#     def init(self,ism,familya,tyil):
#         self.name=ism
#         self.sname=familya
#         self.date=tyil
#         self.bosqich=1
#     def introduce(self):
#         return f'Talaba ismi:{self.name},Familya:{self.sname},yosh:{self.date}bosqich:{self.bosqich}'
#     def get_fullname(self) :
#         return f'My fullname is -{self.name}{self.sname}'
#     def get_age(self,year):
#         return year-self.date
#     def set_level(self,bosqich):
#         self.bosqich=bosqich   
#     def level_oshir(self):
#         self.bosqich=self.bosqich+1  
#     def get_name(self):
#         return f'{self.name}{self.sname}'     
# talaba1=Talaba('Abrorbek:',' Samiyev',2010)
# talaba2=Talaba('Mustafo:','Samiyev',2022)
# talaba3=Talaba('Nazira:','Karimova',2001)
# # print(talaba1.get_name())
# # print(talaba1.introduce())

# # talaba1.set_level(3)
# # talaba1.level_oshir()
# # print(talaba1.introduce())

# class Fan:
#     def init(self,nomi):
#         self.nomi=nomi
#         self.talabalar_soni=0
#         self.talabalar=[]

#     def get_name(self) :
#         return self.nomi

#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni+=1
#     def get_students(self):
#         return [talaba.get_name() for talaba in self.talabalar]
#     def get_students_num(self):
#         return self.talabalar_soni
# ingliz=Fan('Ingliz tili') 
# ingliz.add_student(talaba1)
# ingliz.add_student(talaba2)
# print(ingliz.talabalar)
# print(ingliz.get_students())
# print(ingliz.get_students_num())

# matem=Fan('Matematika')
# matem.add_student(talaba3)
# print(matem.get_students())
# print(matem.get_students_num())
# print(ingliz.talabalar)            

# print(ingliz.talabalar_soni)          

# print(talaba2.introduce())
# print(talaba1.get_fullname())
# print(talaba1.get_age(2023))

# print(talaba1.name)
# print(talaba1.sname)
# print(talaba1.date)



# class Shaxs:
#     def __init__(self,ism,familya,passport,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.passport=passport
#         self.tyil=tyil
#     def get_info(self):
#         return f'Uning ism-{self.ism}va familyasi-{self.familya}\
#         passport seria:{self.passport} hamda tugilgan yili-{self.tyil}.'
#     def get_age(self,bugun):
#         return bugun-self.tyil

# # person=Shaxs('Alisher','Hamidov','AA1235849',2001)
# # print(person.get_info())
# # print(person.get_age(2023))
# class Manzil:
#     def __init__(self,viloyat,tuman,kocha,uyRaqam):
#         self.viloyat=viloyat
#         self.tuman=tuman
#         self.kocha=kocha
#         self.uyRaqam=uyRaqam

#     def get_manzil(self):
#         info=f'{self.viloyat} viloyat {self.tuman} tumani'
#         info+=f'{self.kocha} kochasi {self.uyRaqam}-uy.'
#         return info

# manzil1=Manzil('Namangan','Kosonsoy','Gulbog',33)
# print(manzil1.get_manzil())

# class Talaba(Shaxs):
#     def __init__(self,ism,familya,passport,tyil,guruhRaqam,manzil):
#         super().__init__(ism,familya,passport,tyil)
#         self.guruhRaqam=guruhRaqam
#         self.bosqich=1
#         self.manzil=manzil

#         def get_bosqich(self):
#             return self.bosqich

#         def get_guruh(self):
#             return self.guruhRaqam

#         def get_info(self):
#             info=f'Uning ism-{self.ism} va familyasi- {self.familya}'
#             info+=f'passport seria-{self.passport} guruhRaqam- {self.guruhRaqam}'
#             info+=f'Talaba bosqichi-{self.bosqich}'
#             info+=f'Talaba - {self.manzil.get_manzil()}da turadi.'
#             return info

# manzil1=Manzil('Namangan','Kosonsoy','Gulbog',33)
# talaba1=Talaba('Nozima','Gulniyozova','AC12555485',1999,'41-ATT-2022')
# print(talaba1.manzil.get_manzil())
# print(talaba1.get_info())
# print(talaba1.get_bosqich())
# print(talaba1.get_guruh())
# print(talaba1.get_info())
# print(talaba1.get_age(2025))





from uuid import uuid4
class Avto:
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            print('Km ozgartirish bolmaydi')

avto1=Avto('Gm','Gentra','kok',2018,15000)
avto2=Avto('toyota','toyota 2','qora',2014,12300,100)
avto1.get_km(22)
print(avto2.get_km())