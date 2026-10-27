from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('bike/<int:bike_id>/',views.bike_details,name='bike_details'),
    path('contact/', views.contact, name='contact'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    

]