from django.urls import path
from . import views 
urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'), 
    path('',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout')
]