from django.urls import path


from app_products import views

app_name = 'products'

urlpatterns = [
    #Class View
    path('',views.ProductListCreateAPIView.as_view(),name='list'),
    path('<slug:slug>/',views.ProductDetailApiView.as_view(),name='detail'),

    # Func view
    # path('',views.products_view,name='list'),
    # path('<slug:slug>/',views.products_detail_view,name='detail'),
]