"""first_local URL Configuration

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
from django.urls import path, include

# upload setting - 파일 업로드를 위한 설정
from django.conf.urls.static import static
from django.conf import settings # settings.py 를 잡아줌


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('sns/', include('sns.urls')),
]

# Dev Only
# DEBUG = False 되면, 자동으로 static => return []
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)