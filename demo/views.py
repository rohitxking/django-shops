from django.shortcuts import render,redirect
from django.urls import path
from django.views import View 
from . forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

from demo.models import(
    Customer,
    Product,
    Cart,
    OrederPlace

)

class productView(View):
    def get(self, request):
        camera = Product.objects.filter(category = 'C')
        men = Product.objects.filter(category = 'M')
        women = Product.objects.filter(category = 'W')
        sunglasses = Product.objects.filter(category = 'S')
        shoes = Product.objects.filter(category = 'Sh')
        context = {
            'camera':camera,
            'men':men,
            'women':women,
            'sunglasses':sunglasses,
            'shoes':shoes
        }
        return render(request, 'index.html', context)
    

class ProductDetails(View):
    def get(self, request ,id):
        product = Product.objects.get(pk = id)
        return render(request, 'details.html', {'product':product})

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html',{'form':form})
    

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation Registred Successfully')
            form.save()
            
          
            return redirect('login')

        return render(request, 'registration.html',{'form':form})



def search(request):
    q = request.GET.get('query')
    data = Product.objects.filter(product_name__icontains = 'query')
    return render(request, 'search.html', {'data':data, 'q': q})


def cart(request):
    user = request.user
    product_id = request.GET.get('pro_id')
    # product = Product.objects.get(pk = product_id)
    customer = User.objects.get(username=user)
    carts = Cart.objects.filter(customer=customer)

    total_price = 0
    for i in carts:
        total_price += i.product.discount_price * i.quantity

    return render(request, 'cart.html', {'carts': carts, 'total':total_price})

def delete(request,id):
    data = Cart.objects.get(pk=id)
    data.delete()
    return redirect('cart')

def profile(request):
    return render(request, 'profile.html')



# def carts(request):
#     user = request.user
#     customer = Customer.objects.get(user=user)
#     carts = Cart.objects.filter(user = customer)

#     total_price = 0
#     for i in carts:
#         total_price += i.product.discounted_price * i.quantity

#     return render(request, 'carts.html', {'carts': carts, 'total':total_price})

def addToCart(request):
    user = request.user
    product_id = request.GET.get('pro_id')
    product = Product.objects.get(pk = product_id)
  
    for user in User.objects.all():
        User.objects.get_or_create(username = user)
    # customer = Customer.objects.get(user = user)

    Cart(customer=request.user, product=product).save()
    return redirect('cart')

def mens(request): 
    em = Product.objects.filter(category = 'M')
    return render(request,'mens.html', {'em': em})


def shoes(request):
    so= Product.objects.filter(category = 'Sh')
    return render(request,'shoes.html', {'so':so})


def women(request):
    wm= Product.objects.filter(category = 'W')
    return render(request,'women.html', {'wm':wm})


def sunglasses(request):
    su= Product.objects.filter(category = 'S')
    return render(request,'sunglasses.html', {'su':su})


def camera(request):
    ca= Product.objects.filter(category = 'C')
    return render(request,'camera.html', {'ca':ca})