from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name = "index"),
    path('add_goods/', views.add_goods, name = "add_goods"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('good_records/', views.good_records, name = "good_records"),
    path('register/', views.register, name = "register"),
    path('tracking/', views.tracking, name = "tracking"),

]