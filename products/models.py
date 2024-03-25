from datetime import datetime
from decimal import Decimal
from email.policy import default
from time import time
from unicodedata import category, name
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='title')
    content = models.TextField(verbose_name='description', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d',default='photos/24/2/28.g.jpeg')
    active = models.BooleanField(default=True)

    x=[
        ('category1','cat1'),
        ('category2','cat2')
    ]
    category =  models.CharField(max_length=50,null=True,blank=True,choices=x)

    def __str__(self):
        return self.name

    class Meta:
        #verbose_name = 'name'
        ordering = ['-price']

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField()
    created = models.DateTimeField(default=datetime.now)