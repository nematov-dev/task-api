from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import views
from rest_framework.exceptions import NotFound

from app_products.serializers import ProductSerialize
from app_products.models import ProductsModel

#Class View

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerialize

class ProductDetailApiView(views.APIView):
    serializer_class = ProductSerialize
    response = {"success": True}

    def get(self,request,slug):
        product = self.get_object(slug=slug)
        serializer = self.serializer_class(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,slug):
        product = self.get_object(slug=slug)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response["data"] = serializer.data
            return Response(data=self.response, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

        
    def patch(self,request,slug):
        product = self.get_object(slug=slug)
        serializer = ProductsModel(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            self.response["data"] = serializer.data
            return Response(data=self.response, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self,request,slug):
        product = self.get_object(slug=slug)
        product.delete()
        self.response["detail"] = "Product is deleted"
        return Response(data=self.response, status=status.HTTP_204_NO_CONTENT)


    def get_object(self,slug):
        try:
            return ProductsModel.objects.get(slug=slug)
        except ProductsModel.DoesNotExist:
            self.response['success'] = False
            self.response['detail'] = "Product does not exists" 
            raise NotFound(self.response)

# Function views

# @api_view(["GET", "POST"])
# def products_view(request):
#     if request.method == "GET":
#         products = ProductsModel.objects.all()
#         serializer = ProductSerialize(products, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == "POST":
#         serializer = ProductSerialize(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE", "PATCH"])
# def products_detail_view(request, slug):
#     response = {"success": True}
#     try:
#         post = ProductsModel.objects.get(slug=slug)
#     except ProductsModel.DoesNotExist:
#         response["success"] = False
#         response["detail"] = "Post does not exists"
#         return Response(data=response, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ProductsModel(post)
#         response["data"] = serializer.data
#         return Response(data=response, status=status.HTTP_200_OK)

#     elif request.method == "PUT":
#         serializer = ProductsModel(post, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             response["data"] = serializer.data
#             return Response(data=response, status=status.HTTP_202_ACCEPTED)

#     elif request.method == "PATCH":
#         serializer = ProductsModel(post, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             response["data"] = serializer.data
#             return Response(data=response, status=status.HTTP_202_ACCEPTED)

#     elif request.method == "DELETE":
#         post.delete()
#         response["detail"] = "Post is deleted"
#         return Response(data=response, status=status.HTTP_204_NO_CONTENT)
    

    




