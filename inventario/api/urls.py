from rest_framework.routers import DefaultRouter
from inventario.api.views import ProductoViewSet



router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')

urlpatterns = router.urls