from django.db import models
from django.utils import timezone


# Create your models here.

class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('OL', 'Oolong'),
        ('HR', 'Herbal'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price=models.CharField(max_length=10,default='10')
    
    def __str__(self):
        return self.name
