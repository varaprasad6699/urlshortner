from django.shortcuts import render,redirect
from link.models import StoreUrlDate
import uuid
from django.utils import timezone
from datetime import datetime
# Create your views here.
def home(request):
    total_links=StoreUrlDate.objects.all().count()
    today=datetime.today().strftime('%Y-%m-%d')
    today_taps=StoreUrlDate.objects.filter(currentdate=today).count()
    print(total_links)
    if request.method=='POST':
        print("entered inside........")
        link=request.POST.get('link')
        print(link)
        x=uuid.uuid4()
       # date=timezone.now
        x=str(x)[:5]
        data=StoreUrlDate(link=link,uuid=x)
        data.save()
        total_links=StoreUrlDate.objects.all().count()
        today=datetime.today().strftime('%Y-%m-%d')
        today_taps=StoreUrlDate.objects.filter(currentdate=today).count()
        print(x)
        return render(request,'index.html',{'uuid':x,'total_links':total_links,'today_taps':today_taps,'link':link})
    return render(request,'index.html',{'uuid':'','total_links':total_links,'today_taps':today_taps})
def nextLink(request,id):
    data=StoreUrlDate.objects.get(uuid=id)
    print(data)
    link=data.link
    print(link)
    return redirect(link)