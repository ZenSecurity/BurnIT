"""burnit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter
from gallery.views import SymbolViewSet
from poll.views import UserViewSet, PollViewSet

api_router = DefaultRouter()
api_router.register(r'gallery', SymbolViewSet)
api_router.register(r'user', UserViewSet)
api_router.register(r'poll', PollViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='frontend/index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls, namespace='api')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
