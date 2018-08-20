from django.urls import path

from . import views
app_name = 'awb'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/logout',views.logout_view, name='logout'),
    path('createcoversheet',views.form_creation, name='createcoversheet'),
    path('accounts/createresearcher', views.create_researcher, name='create_researcher'),
]
