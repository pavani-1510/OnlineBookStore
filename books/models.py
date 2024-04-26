from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Book(models.Model):
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    highlights = models.TextField(max_length=500, default=None, blank=True)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, default=False)
    follow_author = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField(default=False)
    total_ratings = models.IntegerField(default=0)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"

class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.title
