from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet, UserViewSet

# Настройка маршрутов для API
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
