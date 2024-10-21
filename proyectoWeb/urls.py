"""
URL configuration for proyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("physimathcode/", include("physimathcode.urls")),
    # path("cursos/", include("cursos.urls")),
    path("fisicalab1/", include("fisicalab1.urls")),
    path("fisicalab2/", include("fisicalab2.urls")),
    path("autenticacion/", include("autenticacion.urls")),
    path("visualizacionfiles/", include("visualizacionfiles.urls")),
    path("classroom/", include("classroom.urls")),
    path("infocurricular/", include("infocurricular.urls")),
    path("publications/", include("publications.urls")),
    path("gallery/", include("gallery.urls")),
    path("research/", include("research.urls")),
    path("portafolio/", include("portafolio.urls")),
    path("contact/", include("contact.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
