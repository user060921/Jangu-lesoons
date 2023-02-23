# from uuid import uuid4


# class Avto:
#     num_avto = 0

#     def init(self, make, model, rang, yil, narx, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#         Avto.num_avto+1

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         if km >= 0:
#             self.__km += km

#         else:
#             print('Km ozgartirib bolmaydi')

#     def __repr__(self):
#         info="""
#         Avto Obyekti mashinalara haqida hususiyatlar va
#         metodlariga ega obyekt hisoblanadi
        
        
#         """
#         return info

#     def __le___(self,other):
#         return self.narx<=other.narx

#     def __lt___(self,other):
#         return self.narx<=other.narx

#     def __gt___(self,other):
#         return self.narx<=other.narx

#     def __ge___(self,other):
#         return self.narx>=other.narx

#     def __eq___(self,other):
#         return self.narx==other.narx

# avto1 = Avto('GM', 'Gentra', 'kok', 2018, 15800)
# avto2 = Avto('Toyota', 'Toyota 2', 'Qongiz', 2004, 12300, 100)

# print(avto1<=avto2)
# print(avto1<avto2)
# print(avto1>avto2)
# print(avto1>=avto2)
# print(avto1==avto2)
# print(avto1!=avto2)

class Bank_record:
    def init(self,name):
        self.name=name
    def call(self):
        return 2**2
bank1=Bank_record('Anna')
print(bank1)














# print(avto1.get_id())
# print(avto2.get_km())
# print(dir(avto1))
# print(dir('Hello world'))
# avto1.add_km(22)
# print(avto1.get_km())
# print(avto1)