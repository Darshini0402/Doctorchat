from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path('doctor.html', views.doc, name="doc"),
    path("logout", views.logout_view, name="logout"),
    path('user.html', views.user,name='user'),
    path('sign.html',views.sign,name='sign'),
    path('book.html',views.book,name='book'),
    path('appointment.html',views.appointment,name='appointment'),
    path('billing.html',views.billing,name='billing'),
    path('option.html',views.option,name="option"),
    path('edit.html',views.edit,name='edit'),
    path('cancel.html',views.cancel,name='cancel.html'),
    path('template.html',views.template,name='template'),
    path('feedback.html',views.feedback,name="feedback"),
   # path('billing.html',views.transaction,name='transaction'),
]