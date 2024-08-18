from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SSTViewSet, ROViewSet, RMMCQViewSet, PracticeHistoryViewSet

router = DefaultRouter()
router.register(r'sst', SSTViewSet)
router.register(r'ro', ROViewSet)
router.register(r'rmmcq', RMMCQViewSet)
router.register(r'practice-history', PracticeHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
