from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path('doctor.html', views.doc, name="doc"),
    path("logout", views.logout_view, name="logout"),
    path('user.html', views.user,name='user'),
    path('sign.html',views.sign,name='sign'),
    path('book.html',views.book,name='book'),
    path('appointment.html',views.lappointment,name='lappointment'),
    path('chat.html',views.chat,name='chat'),
    path('billing.html',views.billing,name='billing'),
]