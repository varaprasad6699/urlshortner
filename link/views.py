from django.shortcuts import render,redirect
from link.models import StoreUrlDate,IpAddress
import uuid
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
# Create your views here.
def home(request):
    total_links=StoreUrlDate.objects.all().count()
    today=datetime.today().strftime('%Y-%m-%d')
    today_taps=StoreUrlDate.objects.filter(currentdate=today).count()
    print(total_links)
    #### get ip address  ###
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_client_ip(request)
    print("ip address",ip) 
    user=IpAddress(user_ip=ip)
    exists=IpAddress.objects.filter(user_ip=ip).count()
<<<<<<< HEAD
    print("exists",exists)
    if exists==1:
=======
    if exists=1:
>>>>>>> fec9460462d8b750b52bce8697952c4e1e0b2659
        print("how many same",exists)
    else:
        user.save()
    ip_count=IpAddress.objects.all().count()
    print("ip count",ip_count)
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
     
        return render(request,'index.html',{'uuid':x,'total_links':total_links,'today_taps':today_taps,'link':link,'ip_count':ip_count})
    return render(request,'index.html',{'uuid':'','total_links':total_links,'today_taps':today_taps,'ip_count':ip_count})

def nextLink(request,id):
    data=StoreUrlDate.objects.get(uuid=id)
    print(data)
    link=data.link
    print(link)
    return redirect(link)
