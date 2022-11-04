from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.admin_index, name='admin_index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('user-edit/', views.user_edit, name='user_edit'),
    path('user-pro/<int:id>',views.edituser_single,name='edituser_single'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('unblock/<int:id>',views.unblock,name='unblock'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
    path('tax_edit/',views.tax_edit,name='tax_edit'),
    path('tax_add/', views.tax_add, name='tax_add'),
    path('tax_delete/<int:id>', views.tax_delete, name='tax_delete'),
    path('order-details/',views.order_details,name='order_details'),
    path('vendor-approval/',views.vendor_approval,name='vendor_approval'),
    path('vendor-profile/<int:id>',views.vendor_profile,name='vendor_profile'),
    path('activate_vendor/<int:id>',views.activate_vendor,name='activate_vendor'),
    path('deactivate_vendor/<int:id>',views.deactivate_vendor,name='deactivate_vendor'),
    
    path('edit-order/<int:id>',views.edit_order ,name="edit_order"),
    path('revenue/', views.revenue,name="revenue"),
    path('details/',views.details,name='details'),
    path('staff-details/',views.staff_details,name='staff_details'),
    
    path('refund_request/', views.refund_request,name="refund_request"),
]