from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
numeric = RegexValidator(r'^[0-9+]','Only digit characters.')
class Client(models.Model):
    category =( 
        ('Website type','--Select Website type'),
        ('Static WebSite','Static Website'),
        ('Dynamic Website','Dynamic Website')
    )
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=10,blank=True,validators=[numeric])
    email = models.EmailField(max_length=100,null=True)
    web_category = models.CharField(max_length=100,choices = category,null=True,default='Website type')
    web_description = models.TextField(max_length=1000,null=True)
    def __str__(self):
        return self.name
