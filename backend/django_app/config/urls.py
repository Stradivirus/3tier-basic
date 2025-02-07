# urls.py 수정
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/admin/', admin.site.urls),
]