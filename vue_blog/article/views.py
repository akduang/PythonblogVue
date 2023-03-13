from django.shortcuts import render
# article/views.py
from django.http import JsonResponse
from django.http import Http404

from article.models import Article

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from article.permissions import IsAdminUserOrReadOnly
from rest_framework import filters

from rest_framework import viewsets
from article.serializers import ArticleSerializer
from article.models import Category

from article.serializers import CategorySerializer, CategoryDetailSerializer

from article.models import Tag
from article.serializers import TagSerializer

from article.serializers import ArticleDetailSerializer

# from article.serializers import ArticleDetailSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ArticleSerializer
    #     else:
    #         return ArticleDetailSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
    
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
          
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True,context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 新增
    # permission_classes = [IsAdminUser]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]