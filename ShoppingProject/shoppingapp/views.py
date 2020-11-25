from django.shortcuts import render,redirect
from django.views.generic.base import View

from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import  login_required
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger

if __name__ == '__main__':
    from django.contrib import messages


# Create your views here.



@login_required(login_url='login_signin')
def cloths(request):
    return render(request, 'cloths.html', )

@login_required(login_url='login_signin')
def women_menu(request):
    return render(request, 'women_menu.html')

@login_required(login_url='login_signin')
def shirts(request):
    res = ProductModel.objects.all()
    return render(request, 'shirts.html', {'allpro': res})

@login_required(login_url='login_signin')
def shoe(request):
    return render(request, 'shoe.html')

@login_required(login_url='login_signin')
def bags(request):
    return render(request, 'bags.html')

@login_required(login_url='login_signin')
def watches(request):
    res = ProductModel.objects.filter(product_categire=10)
    return render(request, 'watches.html', {'res': res})

@login_required(login_url='login_signin')
def goggules(request):
    res = ProductModel.objects.filter(product_categire=12)
    return render(request, 'goggules.html', {'res': res})

@login_required(login_url='login_signin')
def categires(request):
    return render(request, 'categires.html')

@login_required(login_url='login_signin')
def formal(request):
    res = ProductModel.objects.filter(product_categire=1)


    return render(request, 'formal.html', {'model': res})

@login_required(login_url='login_signin')
def suites(request):
    res = ProductModel.objects.filter(product_categire=2)
    return render(request, 'suites.html', {'res': res})

@login_required(login_url='login_signin')
def kurthas(request):
    res = ProductModel.objects.filter(product_categire=3)
    return render(request, 'kurthas.html', {'res': res})

@login_required(login_url='login_signin')
def tshirts(request):
    res = ProductModel.objects.filter(product_categire=4)
    return render(request, 'tshirts.html', {'res': res})

@login_required(login_url='login_signin')
def casuals(request):
    res = ProductModel.objects.filter(product_categire=5)
    return render(request, 'casuals.html', {'res': res})

@login_required(login_url='login_signin')
def sarees(request):
    res = ProductModel.objects.filter(product_categire=6)
    return render(request, 'sarees.html', {'res': res})

@login_required(login_url='login_signin')
def l_kurthas(request):
    res = ProductModel.objects.filter(product_categire=7)
    return render(request, 'l_kurthas.html', {'res': res})

@login_required(login_url='login_signin')
def dresses(request):
    res = ProductModel.objects.filter(product_categire=8)
    return render(request, 'dresses.html', {'res': res})

@login_required(login_url='login_signin')
def half_sarees(request):
    res = ProductModel.objects.filter(product_categire=13)
    return render(request, 'half_sarees.html', {'res': res})

@login_required(login_url='login_signin')
def kids_half(request):
    res = ProductModel.objects.filter(product_categire=14)
    return render(request, 'kids_half.html', {'res': res})

@login_required(login_url='login_signin')
def kids_dresses(request):
    res = ProductModel.objects.filter(product_categire=15)
    return render(request, 'kids_dresses.html', {'res': res})

@login_required(login_url='login_signin')
def kids_boys_dresses(request):
    res = ProductModel.objects.filter(product_categire=16)
    return render(request, 'kids_boys_dresses.html', {'res': res})

@login_required(login_url='login_signin')
def clgbags(request):
    res = ProductModel.objects.filter(product_categire=19)
    return render(request, 'clgbags.html', {'res': res})

@login_required(login_url='login_signin')
def backpack(request):
    res = ProductModel.objects.filter(product_categire=18)
    return render(request, 'backpack.html', {'res': res})

@login_required(login_url='login_signin')
def h_bags(request):
    res = ProductModel.objects.filter(product_categire=17)
    return render(request, 'h-bags.html', {'res': res})

@login_required(login_url='login_signin')
def formsl_shoes(request):
    res = ProductModel.objects.filter(product_categire=20)
    return render(request, 'formsl_shoes.html', {'res': res})

@login_required(login_url='login_signin')
def casual_shoes(request):
    res = ProductModel.objects.filter(product_categire=21)
    return render(request, 'casuals_shoes.html', {'res': res})

@login_required(login_url='login_signin')
def buy_product(request):

     pname = request.GET.get('pname')
     pprice= request.GET.get('pprice')


     pimage = request.GET.get('pimage')

     res=ProductModel.objects.filter( product_name=pname,product_price=pprice,product_image=pimage)

     return render(request, 'buy_product.html',{'res':res})

@login_required(login_url='login_signin')
def buy_add(request):
    return render(request,'buy_add.html')

@login_required(login_url='login_signin')
def men(request):
    return render(request,'men.html')

@login_required(login_url='login_signin')
def kids(request):

    return render(request,'kids.html')

@login_required(login_url='login_signin')
def boath(request):

    return render(request, 'boath.html')

@login_required(login_url='login_signin')
def menu(request):

    return render(request, 'menu.html')


def login_signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        error = False
        if request.method == 'POST':
            dic = request.POST
            usr = dic['user']
            pwd = dic['pwd']
            user = authenticate(username=usr, password=pwd)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True
        return render(request, 'login_signin.html', {'error': error})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        error = False
        if request.method == 'POST':
            dic = request.POST
            u = dic['user']
            p = dic['pwd']

            e = dic['email']
            m = dic['mob']
            a = dic['add']
            i = request.FILES['img']
            userdata = User.objects.filter(username=u)
            if not userdata:
                user = User.objects.create_user(username=u, password=p, email=e)
                UserDetail.objects.create(usr=user, image=i, mobile=m, address=a)
                return redirect('login_signin')
            else:
                error = True
        return render(request, 'signup.html', {'error': error})


def logoutt(request):
    logout(request)
    return redirect('home')




def add_to_cart(request,pk):
   prodata=ProductModel.objects.get(product_id=pk)
   usr = request.user
   caedata=AddtocartModel.objects.filter(usr=usr,pro=prodata).first()

   if request.method == 'POST':

       price = request.POST['price']

       quantity = request.POST['pquantity']
       size = request.POST['size']
       total = float(price) * int(quantity)
       if caedata:

            return render(request,'buy_product.html',{'message':'sorry this item  is already added'})
       else:
           AddtocartModel.objects.create(usr=usr, pro=prodata, quantity=quantity, total_price=total, size=size)
   return redirect('view_cart')





def view_cart(request):
    cartdata = AddtocartModel.objects.filter(usr=request.user)
    g_total = 0
    for i in cartdata:
        g_total += i.total_price
    return render(request,'view_cart.html',{'total':g_total})


def remove_cart(request,pk):
    print(pk)
    AddtocartModel.objects.filter(pro__product_id=pk).delete()
    return redirect('view_cart')

from  .forms import  *
import random


class Checkout(View):
    def get(self,request,pk=None):
        form=OrderForm()
        return render(request,'checkout.html',{'form':form})

    def post(self,request,pk):
        print('hghavv gs')
        ran=random.randint(100000000,85744585525)

        prodata=AddtocartModel.objects.get(pro__product_id=pk)
        print('pk=',pk)
        fname=request.POST['fullname']
        mobile = request.POST['mobile']
        alt_mbl = request.POST['alternative_mobile']
        house = request.POST['house_no']
        area = request.POST.get('area')
        addr1 = request.POST['address1']
        addr2 = request.POST['address2']
        pinc = request.POST['pincode']
        order_status='confirmed'

        print(fname)
        OrderModel.objects.create(usr=request.user,
                                  pro=prodata.pro,
                                  fullname=fname,
                                  mobile=mobile,
                                  alternative_mobile=alt_mbl,house_no=house,
                                  area=area,address1=addr1,address2=addr2,
                                  pincode=pinc,order_id=ran,amount=prodata.total_price,
                                  order_status=order_status)
        addd=AddtocartModel.objects.filter(pro=prodata.pro_id).delete()
        return redirect('view_cart')





def search(request):
    if request.method == 'POST':
     search= request.POST['search']
     print(search)
     if search:
       res= ProductModel.objects.filter(product_categire__categirie__icontains=search)
       print(res)
       print(res)
       if res:
                return render(request,'search.html',{'search':res})
    pass


def dashboard(request):
    profile=UserDetail.objects.filter(usr=request.user)
    print('profile=',profile)
    return render(request,'dashboard.html',{'profile':profile})


def profile(request):
    profile = UserDetail.objects.filter(usr=request.user)
    return render(request,'profile.html',{'profile':profile})


def orders(request):
    profile = OrderModel.objects.filter(usr=request.user)
    return render(request,'orders.html',{'profile':profile})


def shipping(request):
    return render(request,'shipping.html')