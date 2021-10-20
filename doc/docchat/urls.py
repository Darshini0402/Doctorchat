from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("template",views.template, name="template"),
    path('user.html', views.user,name='user'),
]