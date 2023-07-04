from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_demos.web.urls')),
    path('auth/', include('auth_demos.app_auth.urls'))
]