from django.urls import path
from . import views
from . views import RequestRefundView


urlpatterns = [
    path('place-order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

]