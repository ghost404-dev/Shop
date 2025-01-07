from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('Pizza', 'Пицца'),
        ('Rolls', 'Роллы'),
        ('Drinks', 'Напитки'),
    ]
    name = models.CharField(max_length=50,null=True)
    description = models.TextField(max_length=255,default=None)  
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES ,null=True)

    def __str__(self):
        return self.name 
 