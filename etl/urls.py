"""etl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main_page.views import main_view,offer_view
from users.views import register
from destination.views import destination,agra,himachal,ladakh,dharamshala,rajasthan


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view),
    path('home/', main_view),
    path('register/', register, name='register'),
    path('offers/', offer_view, name='offers'),
    path('destination/',destination,name='destinations'),
    path('destination/agra', agra,name='agra'),
    path('destination/himachal', himachal,name='himachal'),
    path('destination/ladakh', ladakh,name='ladakh'),
    path('destination/dharamshala', dharamshala,name='dharamshala'),
    path('destination/rajasthan', rajasthan,name='rajasthan'),
]
