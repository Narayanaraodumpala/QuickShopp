from django.shortcuts import render
from .models import ProductModel

# Create your views here.
def home(request):
    return render(request,'index.html')


def cloths(request):

    return render(request,'cloths.html',)


def women_menu(request):
    return render(request,'women_menu.html')


def shirts(request):
    res=ProductModel.objects.all()
    return render(request,'shirts.html',{'allpro':res})


def shoe(request):

    return render(request,'shoe.html')


def bags(request):

    return render(request,'bags.html')


def watches(request):
    res = ProductModel.objects.filter(product_categire=10)
    return render(request,'watches.html',{'res':res})


def goggules(request):
    res = ProductModel.objects.filter(product_categire=12)
    return render(request,'goggules.html',{'res':res})





def categires(request):

    return render(request,'categires.html')


def formal(request):
    res=ProductModel.objects.filter(product_categire=1)
    return render(request, 'formal.html',{'model':res})


def suites(request):
    res = ProductModel.objects.filter(product_categire=2)
    return render(request, 'suites.html',{'res':res})


def kurthas(request):
    res = ProductModel.objects.filter(product_categire=3)
    return  render(request, 'kurthas.html',{'res':res})


def tshirts(request):
    res = ProductModel.objects.filter(product_categire=4)
    return render(request, 'tshirts.html',{'res':res})


def casuals(request):
    res = ProductModel.objects.filter(product_categire=5)
    return render(request, 'casuals.html',{'res':res})


def sarees(request):
    res = ProductModel.objects.filter(product_categire=6)
    return render(request, 'sarees.html',{'res':res})


def l_kurthas(request):
    res = ProductModel.objects.filter(product_categire=7)
    return render(request, 'l_kurthas.html',{'res':res})


def dresses(request):
    res = ProductModel.objects.filter(product_categire=8)
    return render(request, 'dresses.html',{'res':res})


def half_sarees(request):
    res = ProductModel.objects.filter(product_categire=13)
    return render(request, 'half_sarees.html',{'res':res})


def kids_half(request):
    res = ProductModel.objects.filter(product_categire=14)
    return render(request, 'kids_half.html',{'res':res})


def kids_dresses(request):
    res = ProductModel.objects.filter(product_categire=15)
    return render(request, 'kids_dresses.html',{'res':res})


def kids_boys_dresses(request):
    res = ProductModel.objects.filter(product_categire=16)
    return render(request, 'kids_boys_dresses.html',{'res':res})


def clgbags(request):
    res = ProductModel.objects.filter(product_categire=19)
    return render(request, 'clgbags.html', {'res': res})

def backpack(request):
    res = ProductModel.objects.filter(product_categire=18)
    return render(request, 'backpack.html',{'res': res} )

def h_bags(request):
    res = ProductModel.objects.filter(product_categire=17)
    return render(request, 'h-bags.html',{'res': res} )


def formsl_shoes(request):
    res = ProductModel.objects.filter(product_categire=20)
    return render(request,'formsl_shoes.html',{'res': res})


def casual_shoes(request):
    res = ProductModel.objects.filter(product_categire=21)
    return render(request,'casuals_shoes.html',{'res': res})