from django.shortcuts import render
from bigcube.models import Customer, Menu, Seller, Orderlist
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render (request,"index.html")

def home(request):
    return render (request,"home.html")

def newmenu(request):
    if request.method == 'POST':
        mmenucode = request.POST['menucode']
        mmenuname = request.POST['menuname']
        mmenuprice = request.POST['menuprice']
        data = Menu(menucode=mmenucode,menuname=mmenuname,menuprice=mmenuprice)
        data.save()
        dict = {
            'message':'Data Save'
        }
    else:
        dict = {
            'message':''
        }

    return render (request,"newmenu.html",dict)

def menu(request):
    allmenu = Menu.objects.all()
    dict = {
        'allmenu': allmenu
    }
    return render (request,"menu.html",dict)

def searchmenu(request):
    if request.method == 'GET':
        data = Menu.objects.filter(menucode = request.GET.get("mmenucode"))
        dict = {
            'data': data
        }
        return render (request,"searchmenu.html",dict)
    else:
        return render (request,"searchmenu.html")

def updatemenu(request,menucode):
    data = Menu.objects.get(menucode=menucode)
    dict = {
        'data':data
    }
    return render (request,"updatemenu.html",dict)

def saveupdatemenu(request,menucode):
    mmenuname = request.POST['menuname']
    mmenuprice = request.POST['menuprice']
    data = Menu.objects.get(menucode=menucode)
    data.menuname = mmenuname
    data.menuprice = mmenuprice
    data.save()
    return HttpResponseRedirect(reverse('menu'))

def deletemenu(request,menucode):
    data = Menu.objects.get(menucode=menucode)
    data.delete()
    return HttpResponseRedirect(reverse('menu'))


def newcustomer(request):
    allmenu = Menu.objects.all()
    if request.method == 'POST':
        cphone = request.POST['cphone']
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cmenu = request.POST['cmenu']
        cmenucode = Menu.objects.get(code=cmenu) # kalau ada foreign key, jangan lupa ".get"
        data = Customer(cusphone=cphone, cusname=cname, cusemail=cemail,
                       menucode=cmenucode)
        data.save()

        dict = {
            'allmenu': allmenu,
            'message': "Data Save"
        }
    else:
        dict = {
            'allmenu': allmenu
        }
    return render(request, 'newcustomer.html', dict)

def searchbymenu(request):
    allmenu = Menu.objects.all()
    if request.method == 'GET':
        datamenu = Menu.objects.filter(menucode = request.GET.get('mcodevar'))
        numbercust = len(datamenu)
        dict = {
            'data': datamenu,
            'allmenu': allmenu,
            'mcodevar': request.GET.get('mcodevar'),
            'numcust': numbercust,
        }
    else:
        dict = {
            'allmenu': allmenu
        }
    return render (request,'searchbymenu.html',dict)

def login(request):
    if request.method == 'POST':
        cusphone = request.POST.get('cusphone')
        password = request.POST.get('customerpassword')
        try:
            customer = Customer.objects.get(cusphone=cusphone)
        except Customer.DoesNotExist:
            message = "Invalid Customer Phone"
            return render(request, 'login.html', {'message': message})
        
        if customer is None or customer.customerpassword != password:
            message = "Invalid login credentials"
            return render(request, 'login.html', {'message': message})
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        cphone=request.POST['cusphone']
        cname=request.POST['cusname']
        cemail=request.POST['cusemail']
        cpass=request.POST['customerpassword']

        data = Customer(cusphone=cphone,cusname=cname,cusemail=cemail,customerpassword=cpass)
        data.save()
        return render(request,'login.html')

    else:
        return render(request,'signup.html')