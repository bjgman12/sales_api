from django.urls import path
from .views import OrderLists,OrderDetail

urlpatterns = [
    path('',OrderList.as_view(),name='order_list')
    path('',OrderDetail.as_view(),name='order_detail')
]