from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView,CategoryListCreateAPIView,ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView,OrderListCreateAPIView,OrderRetrieveUpdateDestroyAPIView,OrderItemListCreateAPIView,OrderItemRetrieveUpdateDestroyAPIView
urlpatterns = [
    # Define your URL patterns here
    path('api/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
    path('order-items/', OrderItemListCreateAPIView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='orderitem-detail'),

    # More paths...
]