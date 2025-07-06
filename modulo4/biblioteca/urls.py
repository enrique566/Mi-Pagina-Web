from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sitioweb import views

router = DefaultRouter()
router.register(r'libros', views.LibroViewSet)
router.register(r'sesiones', views.SesionComputadoraViewSet)
router.register(r'registros', views.RegistroTrabajoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]
