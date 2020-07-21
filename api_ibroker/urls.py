from django.urls import path, include
from .views import article_list, article_detail

#djago rest
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
 
urlpatterns = [
    path('article/', article_list),
    path('article/<int:pk>', article_detail),
    path('viewset/', include(router.urls)), #api view
]