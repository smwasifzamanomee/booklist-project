from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .seralizers import categorySerializer, productSerializer, productLineSerializer, productImageSerializer, attributeSerializer, attributeValueSerializer
from .models import category, product, productLine, productImage, attribute, attributeValue
from rest_framework.views import APIView

# Create your views here.

class categoryList(APIView):
    def get(self, request):
        category1 = category.objects.all()
        serializer = categorySerializer(category1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request = request.data
        serializer = categorySerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class categoryDetail(APIView):
    def get(self, request, pk):
        category1 = category.objects.get(id=pk)
        serializer = categorySerializer(category1)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        category1 = category.objects.get(id=pk)
        request = request.data
        serializer = categorySerializer(instance=category1, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category1 = category.objects.get(id=pk)
        category1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class productList(APIView): 
    def get(self, request):
        product1 = product.objects.all()
        serializer = productSerializer(product1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request = request.data
        serializer = productSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class productDetail(APIView):
    def get(self, request, pk):
        product1 = product.objects.get(id=pk)
        serializer = productSerializer(product1)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product1 = product.objects.get(id=pk)
        request = request.data
        serializer = productSerializer(instance=product1, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product1 = product.objects.get(id=pk)
        product1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class productLineList(APIView):
    def get(self, request):
        productLine1 = productLine.objects.all()
        serializer = productLineSerializer(productLine1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class productImageList(APIView):
    def get(self, request):
        productImage1 = productImage.objects.all()
        serializer = productImageSerializer(productImage1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class attributeList(APIView):
    def get(self, request):
        attribute1 = attribute.objects.all()
        serializer = attributeSerializer(attribute1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass

class attributeValueList(APIView):
    def get(self, request):
        attributeValue1 = attributeValue.objects.all()
        serializer = attributeValueSerializer(attributeValue1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
