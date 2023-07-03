from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Houses(models.Model):
    houses=(
        ('bedsitter',' bedsitter'),
        ('two bedroom','two bedroom'),
        ('three bedroom','three bedroom'),
        ('four bedroom','four bedroom'),
    )
    name=models.CharField(choices=houses,blank=True,null=True,max_length=100)
    amount=models.FloatField(max_length=100)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def ImageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class Checkout(models.Model):
    floors=(
        ('first floor','first floor'),
        ('second floor','second floor'),
        ('third floor','third floor'),
        ('fourth floor','fourth floor')
    )
    desc=(
        ('bedsitter',' bedsitter'),
        ('two bedroom','two bedroom'),
        ('three bedroom','three bedroom'),
        ('four bedroom','four bedroom'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    description=models.CharField(choices=desc,null=True,max_length=30)
    floors=models.TextField(choices=floors)
    amount=models.FloatField(max_length=100)
    date_booked=models.DateField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.description


