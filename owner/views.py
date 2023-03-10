from django.shortcuts import render,redirect
from owner.forms import ProductForm
from customer.models import Products
from django.views.generic import CreateView,View,ListView
from django.urls import reverse_lazy


# Create your views here.
class AddProductView(CreateView):
    template_name='addproduct.html'
    form_class=ProductForm
    success_url=reverse_lazy('productlist')


class ProductView(ListView):
    template_name='list.html'
    model=Products
    context_object_name="product"


class ProductsDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Products.objects.get(id=id).delete()
        return redirect('productlist')