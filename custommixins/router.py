from rest_framework import routers
from djangomixin.apiview import NameViewSet , PersonViewSet

router = routers.SimpleRouter()
router.register('name' , NameViewSet)
router.register('person' , PersonViewSet)





