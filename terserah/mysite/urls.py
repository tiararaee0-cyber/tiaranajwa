from django.contrib import admin
from django urls import Path, include 

urlpatterns = [
    Path('admin/', admin.site.urls),
    patf('', include('hello.urls')), # hubungkan ke app hello 
]