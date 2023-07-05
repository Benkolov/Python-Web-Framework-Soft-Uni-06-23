from django.urls import path

from auth_demos.app_auth.views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UserListView.as_view(), name='users_list')
]
