"""mysite URL Configuration

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
from django.urls import path
from django.urls import re_path
from blog import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', views.index),
    path('blog/', views.index),
    path('detail/', views.detail),
    #path('student/', views.student, name='data'),
    path('dt/', views.data, name='dt')
    # re_path('blog/(?P<blog_id>[9][2]\d{4})/(?P<type>[0-9])', views.blog_detail),
    # 编号必须是6位数字，且须92开头
]


