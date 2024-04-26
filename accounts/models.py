from django.db import models

# Create your models here.
class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    #book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


# models.py

from django.contrib.auth.models import User


from django.db import models

class CustomerCareMessage(models.Model):
    message = models.TextField()
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.created_at}'
