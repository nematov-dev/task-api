from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_products.serializers import ProductSerialize
from app_products.models import ProductsModel


@api_view(["GET", "POST"])
def products_view(request):
    if request.method == "GET":
        products = ProductsModel.objects.all()
        serializer = ProductSerialize(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = ProductSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

