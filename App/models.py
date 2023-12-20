from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class TeleData(models.Model):
    user_name = models.CharField(max_length=255)
    contact = models.PositiveBigIntegerField()
    #user_call = ArrayField(models.PositiveIntegerField()) 
    
    def __str__(self):
        return self.user_name
    
class CustomerData(models.Model):
    agent = models.ForeignKey(TeleData, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_contact = models.PositiveBigIntegerField()
 