from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='UI-home'),
    path('orders/', views.orders, name='UI-orders'),
    path('companies/', views.companies, name='UI-companies'),
    path('products/', views.products, name='UI-products'),
    path('test/', views.test, name='UI-test'),
]