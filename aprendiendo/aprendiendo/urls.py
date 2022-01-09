"""aprendiendo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from nuevaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('inicio/',views.index,name="inicio"),
    path('pagina/',views.pagina,name="pagina1"),
    path('pagina/<int:redirigir>',views.pagina,name="pagina1"),
    path('contacto/',views.contacto,name="contacto"),
    path('contacto/<str:nombre>',views.contacto,name="contacto"),
    path('hola-mundo/', views.holaMundo,name="hola"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name='crear_articulo'),
    path('articulo/',views.articulo,name="articulo"),
    path('editar/<str:id>',views.editar_articulo,name='editar'),
    path('articulos/',views.articulos,name='articulos'),
    path('borrar/<int:id>',views.borrar,name='borrar'),
    path('save_article/',views.save_article, name='save'),
    path('create_article/',views.create_article,name='create'),
    path('create_full_article/',views.create_full_article,name='create-full'),
]


