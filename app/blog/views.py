from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article,CustomUser
from .serializers import ArticleSerializer,UserSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

class UserView(APIView):
    queryset = CustomUser
    serializer_class = UserSerializer

    def get(self,request):
        model = CustomUser.objects.all()
        serializer = UserSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ArticleView(APIView):
    queryset = Article
    serializer_class = ArticleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,pk=None):
        if pk:
            try:
                model=Article.objects.get(pk=pk)
                serializer=ArticleSerializer(model)
                return Response(serializer.data)
            except Article.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:    
            model = Article.objects.all()
            serializer = ArticleSerializer(model,many=True)
            return Response(serializer.data)
    
    def post(self,request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def put(self,request,pk):
        try:
            instance = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        serializer = ArticleSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            instance=Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)