
from django.urls import path
from .views import *
# urls.py
from . import views  # Import the views module

from django.urls import path

urlpatterns = [

    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name='detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('Payment/', Payment, name='Payment'),
path('update_rating/<int:pk>/', UpdateRatingView.as_view(), name='update_rating'),
    #path('payment/success/', payment_success_view, name='payment_success'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', search_books, name='search_books'),
    path('review/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
]