from ipaddress import ip_address
from django.shortcuts import render, HttpResponse
from ipware import get_client_ip
import datetime
from django import http

# Create your views here.
def index(request):
    ipaddress = get_client_ip(request)
    current_time = datetime.datetime.now()
    with open('ip_address.txt','at') as f:
        f.write(f"ip address is : {ipaddress[0]} time is : {current_time} \n")
    with open('ipaddress.txt','at') as f:    
        f.write(f"{ipaddress[0]}\n")
    with open('ipaddress.txt','rt') as f:
        ips = f.read()
        ipslist = ips.split('\n')
    if ipslist.count(ipaddress[0]) > 5:
        return http.HttpResponseForbidden('<h1>Forbidden</h1>')
    #print(ipaddress[0], current_time)
    return render(request, 'index.html')



def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




