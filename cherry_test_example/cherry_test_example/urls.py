from django.contrib import admin
from django.urls import path

from cherry_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('', views.main),
    path('red-blue-cars', views.get_red_blue_cars)
]
