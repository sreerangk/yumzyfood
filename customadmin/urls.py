from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.admin_index, name='admin_index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('user-edit/', views.user_edit, name='user_edit'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('unblock/<int:id>',views.unblock,name='unblock'),
    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser'),
  

]