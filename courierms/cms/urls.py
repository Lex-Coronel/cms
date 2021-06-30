from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('tracking/', views.tracking, name="tracking"),
    path('payment/', views.payment, name="payment"),
    path('updatepayment/<str:pk>/', views.updatepayment, name="updatepayment"),
    path('delivery/', views.delivery, name="delivery"),
    path('updatedelivery/<str:pk>/', views.updatedelivery, name="updatedelivery"),
    path('deletedelivery/<str:pk>/', views.deletedelivery, name="deletedelivery"),
    path('displaytracking/', views.displaytracking, name="displaytracking"),
    path('pay_tables/', views.pay_tables, name="pay_tables"),
]
