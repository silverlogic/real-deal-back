from rest_framework.routers import DefaultRouter

from .views import OffersViewSet


router = DefaultRouter(trailing_slash=False)
router.register('offers', OffersViewSet, base_name='offers')


urlpatterns = router.urls
