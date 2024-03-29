"""furniture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from furniapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('furni', views.furni, name="furni"),
    path('worker', views.worker, name="worker"),
    path('cal', views.calculator, name="cal"),
    path('cal1', views.cal, name="cal1"),
    path('c', views.index1, name="c"),
    path('<int:id>/<slug:slug>/', views.detail, name='detail'),
    path('<slug:category_slug>/', views.index1, name='list'),
    path('',include('autho.urls',namespace='autho')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
