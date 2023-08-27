from django.urls import path
from .views import categoryList, productList, productLineList, productImageList, attributeList, attributeValueList, productDetail, categoryDetail


urlpatterns = [
    path('category/', categoryList.as_view(), name='category'),
    path('category/<int:pk>/', categoryDetail.as_view(), name='category-detail'),
    path('product/', productList.as_view(), name='product'),
    path('product/<int:pk>/', productDetail.as_view(), name='product-detail'),
    path('productLine/', productLineList.as_view(), name='productLine'),
    path('productImage/', productImageList.as_view(), name='productImage'),
    path('attribute/', attributeList.as_view(), name='attribute'),
    path('attributeValue/', attributeValueList.as_view(), name='attributeValue'),
]