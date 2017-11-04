from django.db import models
from django.core.urlresolvers import reverse

class Product_Form(models.Model):

    lower_limit=models.CharField(max_length=5)
    upper_limit=models.CharField(max_length=5)
    email=models.EmailField()
    file1 = models.FileField()



# Create your models here.
