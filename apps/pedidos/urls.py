from django.urls import path, include
from rest_framework import routers
#from .views import AuthApiList, RolApiList, UsuarioApiList
#from .viewsets import AuthViewSets, RolViewSets, UsuarioViewSets
from .viewsets import RolHypViewSet, ColaboradorHypViewSet
from .viewsets import TipoIngredienteHypViewSet, IngredienteHypViewSet
from .viewsets import EstadoPedidoHypViewSet, PedidoHypViewSet, DetallePedidoHypViewSet

router = routers.DefaultRouter()

#HYPERLINKEDSERIALIZER - viewsets
router.register(r'colaborador', ColaboradorHypViewSet)
router.register(r'rol', RolHypViewSet)
router.register(r'Ingredientes', IngredienteHypViewSet)
router.register(r'TipoIngredientes', TipoIngredienteHypViewSet)
router.register(r'EstadoPedidos', EstadoPedidoHypViewSet)
router.register(r'DetallePedidos', DetallePedidoHypViewSet)
router.register(r'Pedidos', PedidoHypViewSet)

urlpatterns = [
    path('', include(router.urls))
]
