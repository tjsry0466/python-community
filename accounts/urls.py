from django.urls import include, path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('register/done/',
         views.UserCreateDoneTemplateView.as_view(), name='register_done'),
]
