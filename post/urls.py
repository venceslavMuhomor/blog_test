"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import home, add_post, post_detail, add_comment, PostApiView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('add_post', add_post, name='add_post'),
    path('post_detail/<slug:slug>', post_detail, name='post_detail'),
    path('add_comment/<slug:slug>', add_comment, name='add_comment'),
    path('api/get_posts', PostApiView.as_view(), name='post_api')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
