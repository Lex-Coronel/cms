from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('tracking/', views.tracking, name="tracking"),
    path('payment/', views.payment, name="payment"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('delivery', views.delivery, name="delivery"),
    path('displaytracking/', views.displaytracking, name="displaytracking"),

]
