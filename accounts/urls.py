from django.urls import path
from accounts.views import *

urlpatterns = [
   
    # path('<slug>/' , get_product , name="get_product"),
    path('login/',login_page,name="login"),
    path('signup/',register_page,name="signup")



    # 
  
    
]
