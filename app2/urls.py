from django.urls import path,include
from. import views

urlpatterns = [
    path('heloo',views.TestFun,name='heloo')
]