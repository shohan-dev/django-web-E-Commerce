from django.urls import path
from ecom.views import *

urlpatterns = [
   
    # path('<slug>/' , get_product , name="get_product"),
    path('', index),
]
