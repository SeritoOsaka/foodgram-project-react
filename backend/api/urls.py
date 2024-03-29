from django.urls import include, path
from rest_framework import routers

from .views import (IngredientViewSet, RecipeViewSet, TagViewSet,
                    UserSubscriptionViewSet)

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('users', UserSubscriptionViewSet, basename='users')
router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('recipes', RecipeViewSet, basename='recipes')
router_v1.register('ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
