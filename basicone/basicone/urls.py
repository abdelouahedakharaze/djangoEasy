
from django.contrib import admin
from django.urls import path ,include
from easy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.wellcome, name='wellcome'),
]
