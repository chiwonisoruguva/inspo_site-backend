from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PinViewSet, BoardViewSet, SavedPinViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("pins", PinViewSet)
router.register("boards", BoardViewSet)
router.register("saved-pins", SavedPinViewSet)

urlpatterns = router.urls