from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('todos/', include('todo_app.api_todos.urls')),
        path('auth/', include('todo_app.api_auth.urls')),
    ])),
]
