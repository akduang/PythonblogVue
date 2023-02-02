# article/urls.py

from django.urls import path
from article import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from article import views

app_name = 'article'

router = routers.SimpleRouter()
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    # path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    
]

urlpatterns += router.urls