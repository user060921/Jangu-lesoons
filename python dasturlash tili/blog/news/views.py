from django.shortcuts import render
from django.http import HttpResponse
import requests
def home(request):
    ismlar=['Isroil','Boburmirzo','Jahongir','Madina','Gulshida']
    mevalar=['Olma','Anor','Behi','Gilos']
    context={
        'ismlar':ismlar,
        'mevalar':mevalar
    }
    return render(request,'home.html',context)


def about(request):
    data=requests.get('https://restcountries.com/v2/all').json()
    context={
        'countries':data
    }
    return render(request,'about.html',context)

def contact(request):

    if request.method=='POST':
        name=request.POST['fullname']
        contact_number=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        massage=request.POST['text']
        data=ContactUs(
            fullname=name,phone=contact_number,email=email,
            subject=subject,text=massage
        )
        data.save()
    print(request.POST)
    return render(request,'contact.html')



















    # return HttpResponse('Men home page man')

    # return HttpResponse('<h1 style="color:red;">Saytimizning About qismi</h1>')

    # return HttpResponse('<h1 style="color:blue;">Saytimizning contact qismi</h1>')




# def login(request):
    # return HttpResponse('saytning login qismi')

# def signup(request):
    # return HttpResponse('saytning signup qismi')
    

