from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from customer.forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from customer.models import Products,Userprofile,Carts
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
# Create your views here.




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect('signin')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,never_cache]



class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account created successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"account creation failed ")
        return super().form_invalid(form)



class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)               
                return redirect("home")
            else:
                messages.error(request,"Invalid credentials")
                return render(request,"login.html",{"form":form})


@method_decorator(decs,name="dispatch")
class HomeIndexView(ListView):
    template_name="home.html"
    model=Products
    context_object_name="product" 
    
  

@method_decorator(decs,name="dispatch")
class ProfileView(TemplateView):
    template_name="profile.html"


@method_decorator(decs,name="dispatch")

class NonVegView(ListView):
    template_name="home.html"
    model=Products
    context_object_name="product"

    def get_queryset(self):
        return Products.objects.filter(category="nonveg")


@method_decorator(decs,name="dispatch")
class VegView(ListView):
    template_name="home.html"
    model=Products
    context_object_name="product"

    def get_queryset(self):
        return Products.objects.filter(category="veg")




# @method_decorator(decs,name="dispatch")

def addto_Cart(request,*args,**kwargs):
    id=kwargs.get("id")
    product=Products.objects.get(id=id)
    user=request.user
    Carts.objects.create(user=user,product=product)
    messages.success(request,"item has been added to wishlist")
    return redirect("cartlist")



@method_decorator(decs,name="dispatch")

class CartView(ListView):
     template_name="cart.html"
     model=Carts
     context_object_name="items"

     def get_queryset(self):
         return Carts.objects.filter(user=self.request.user)
     


# @method_decorator(decs,name="dispatch")
   
def delete_cart(request,*args,**kwargs):
    id=kwargs.get("id")
    Carts.objects.get(id=id).delete()
    return redirect("cartlist")


@method_decorator(decs,name="dispatch")
class OrderView(TemplateView):
    template_name="checkout.html"
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        qs=Products.objects.get(id=pid)
        return render(request,"checkout.html",{"product":qs})


def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect('signin')