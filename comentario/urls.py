from rest_framework import routers
from comentario.api.viewsets import  ComentarioViewSets


router = routers.DefaultRouter()
router.register('comentario', ComentarioViewSets, 'comentario') # EndPoint 

urlpatterns = router.urls