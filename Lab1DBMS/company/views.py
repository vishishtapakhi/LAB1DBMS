from django.shortcuts import render
from django.http import HttpResponse
from .models import xyzcompany
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# Create your views here.

def home(request):
    peoples = [
        {'name':'xyz','age':26},
        {'name':'abc','age':23},
        {'name':'def','age':24}
    ]
    return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
    return HttpResponse("Hello")

def allinterns(request):
    interns = xyzcompany.objects.all()
    
    return render(request,'index.html',{'interns':interns})

# from django.shortcuts import render

def intern_list_view(request):
    location = request.GET.get('location')
    
    if location:
        interns = xyzcompany.objects.filter(Location=location)
    else:
        interns = xyzcompany.objects.all()
    
    return render(request, 'index.html', {'interns': interns})

def search_intern(request):
    found=False
    if request.method == "POST":
        searched = request.POST['searched']
        interns = xyzcompany.objects.filter(Q(InternID=searched) | Q(ManagerID=searched) | Q(TeamID=searched))
       
        
        return render(request,'index.html',{'searched':searched,'interns':interns,'found':found})
        
    else:
        return render(request,'index.html',{})
# @login_required
# def search_intern(request):
    