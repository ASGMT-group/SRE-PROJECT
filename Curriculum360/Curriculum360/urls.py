
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('users', include('users.urls')),
    path('studyroom', include('baseapp.urls'))
    #path('users', include('django.contrib.auth.urls'))
]


