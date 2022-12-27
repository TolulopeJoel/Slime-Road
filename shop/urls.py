from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('<int:creator_id>/', views.creator_product_list, name='product_list'),
    path('<int:creator_id>/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]