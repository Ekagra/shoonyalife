from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RetreatViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'retreats', RetreatViewSet)
router.register(r'book', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]