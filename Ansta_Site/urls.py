"""Ansta_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from killer_list.views import people_list_view, people_add
#people_edit


urlpatterns = [
    path('', people_list_view, name="Home"),
    path('add_people/', people_add),
   # path('edit_people/<int:my_id>/', people_edit),
    path('admin/', admin.site.urls),
]
