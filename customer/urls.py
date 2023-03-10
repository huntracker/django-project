from django.urls import path
from customer import views



urlpatterns=[
   
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home",views.HomeIndexView.as_view(),name="home"),
    path("addtocart/<int:id>",views.addto_Cart,name="cartadd"),
    path("cartlist",views.CartView.as_view(),name="cartlist"),
    path('deleteitem/<int:id>',views.delete_cart,name='deleteitem'),
    path("checkout/<int:id>",views.OrderView.as_view(),name="checkout"),
    path("NonVeg",views.NonVegView.as_view(),name="nonveg"),
    path("Veg",views.VegView.as_view(),name="veg"),
    path("profile",views.ProfileView.as_view(),name="profile"),
    path("logout",views.SignOutView,name="signout"),
 



]