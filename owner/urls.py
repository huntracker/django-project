from django.urls import path
from owner import views



urlpatterns=[
     path("",views.AddProductView.as_view(),name="addproduct"),
     path('list',views.ProductView.as_view(),name='productlist'),
     path('delete/<int:id>',views.ProductsDeleteView.as_view(),name='deleteitems')
    

]