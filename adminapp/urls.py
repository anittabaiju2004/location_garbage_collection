from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'), 
    path('',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('admin/view-drivers/', views.admin_view_driver, name='admin_view_driver'),
    path('admin/approve-driver/<int:driver_id>/', approve_driver, name='approve_driver'),
    path('admin/reject-driver/<int:driver_id>/', reject_driver, name='reject_driver'),
     path('admin/view-approved-drivers/', view_approved_drivers, name='view_approved_drivers'),
    path('admin/view-rejected-drivers/', view_rejected_drivers, name='view_rejected_drivers'),
    path('admin/view-complaints/', view_complaints, name='view_complaints'),
     path('admin/allocate-complaint/<int:complaint_id>/', allocate_complaint, name='allocate_complaint'),
    path('admin/assign-driver/<int:complaint_id>/<int:driver_id>/', assign_driver, name='assign_driver'),
     path('update-bin-status/<int:complaint_id>/<str:status>/', update_bin_status, name='update_bin_status'),


]
