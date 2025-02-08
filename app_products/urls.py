from django.urls import path


from app_products import views

app_name = 'posts'

urlpatterns = [
    path('',views.products_view,name='list')
]