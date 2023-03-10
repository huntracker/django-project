from django.db import models
from django.contrib.auth.models import User



class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=200,null=True)



class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(upload_to="productimg",null=True)

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


class Carts(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    options=(
        ('order-placed','order-placed'),
        ('in-cart','in-cart'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=200,choices=options,default='in-cart')


class Reviews(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.comment



class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ('order-placed','order-placed'),
        ('despatched','despatched'),
        ('in-transit','in-transit'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=200,choices=options,default='order-placed')
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)

