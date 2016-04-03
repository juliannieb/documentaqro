"""documentaqro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from docu import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^patrocinadores/', views.patrocinadores, name='patrocinadores'),
    url(r'^nosotros/', views.nosotros, name='nosotros'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^blog-post/(?P<post_id>[0-9]+)', views.blog_post, name='blog_post'),
    url(r'^search-blog-posts/', views.search_blog_posts, name='search_blog_posts'),
    url(r'^contacto/', views.contacto, name='contacto'),
    url(r'^evento/(?P<festival_id>[0-9]+)$', views.evento, name='evento'),
    url(r'^evento/(?P<evento_id>[0-9]+)/seleccion-oficial/', views.seleccion_oficial, name='seleccion_oficial'),
    url(r'^evento/(?P<evento_id>[0-9]+)/seleccion-oficial-filtro/(?P<tipo_seleccion>[a-z]+)', views.seleccion_oficial_filtro, name='seleccion_oficial_filtro'),
    url(r'^pelicula/(?P<pelicula_id>[0-9]+)', views.pelicula, name='pelicula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
