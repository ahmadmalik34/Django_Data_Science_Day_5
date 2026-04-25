from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    path('create-post/', views.create_post, name='create_post'),
    path('edit-post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),
]