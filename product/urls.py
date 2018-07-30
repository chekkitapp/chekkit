from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.add_productlines, name='add_productlines'),
    path('<uuid:uuid>/', views.product_line, name='detail_productline'),
    path('generate/', views.generate_product_codes, name='generate_product_codes'),
    path('generate/<uuid:uuid>', views.generate_product_codes, name='generate_product_line_codes'),
    path('productcodes/', views.view_product_codes, name='view_product_codes'),


]
