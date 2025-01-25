from rest_framework import routers
from .views import RecipeViewSet

router = routers.DefaultRouter()

router.register('recipe', RecipeViewSet, basename='recipe')

urlpatterns = router.urls
