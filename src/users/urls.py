from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as user_views

urlpatterns = [
    path('login/', user_views.CustomLoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name='logout'),

    path('profile/', user_views.profile, name="profile"),
    path('org_register/', user_views.organizerRegister, name="org-register"),
]
