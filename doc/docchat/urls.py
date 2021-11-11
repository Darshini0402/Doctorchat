from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path('doctor.html', views.doc, name="doc"),
    path("logout", views.logout_view, name="logout"),
    path("template.html",views.template, name="template"),
    path('user.html', views.user,name='user'),
    path('sign.html',views.sign,name='sign'),
    path('template.html',views.template,name='template'),
]