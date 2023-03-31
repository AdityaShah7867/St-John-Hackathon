from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home,name='home'),

    
    
    
   
    path('login/', views.loginR,name='loginR'),
    path('logout/',views.logoutR,name='logout'),
   
    path('register/',views.registerR,name='register'),
    path('notes/',views.notes,name='notes'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('first/',views.first,name='first')
    
    

]