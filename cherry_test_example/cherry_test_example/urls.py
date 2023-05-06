from django.contrib import admin
from django.urls import path

from cherry_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('red-blue-cars', views.get_red_blue_cars),
    path('register-owner-car', views.register_car_owner),
    path('register', views.register),
    path('old-owner', views.get_old_owners_cars),
    path('Cars-on-road', views.get_heavy_cars),
    path('tolls-of-car', views.find_tolls_of_cars),
    path('find_tolls', views.find_tolls),
    path('location-lists', views.get_location_lists),
    path('name-and-national-code', views.show_name_national_code)
]
