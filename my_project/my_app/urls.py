from django.urls import path
from .views.main_view import index, create_todo, single_page, edit_todo, delete_todo
from .views.auth_view import register_page, login_page, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_user, name='logout'),
    path('create/', create_todo, name='create_todo'),
    path('single/<int:id>/', single_page, name='single'),
    path('edit/<int:id>/', edit_todo, name='edit_todo'),
    path('delete/<int:id>/', delete_todo, name='delete_todo'),
] 