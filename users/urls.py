from django.urls import path
from users.views import create_user, get_users, get_user, update_user, delete_user

urlpatterns = [
    path('', get_users, name='get_users'),
    path('create/', create_user, name='create_user'),
    path('<int:user_id>/', get_user, name='get_user'),
    path('<int:user_id>/update/', update_user, name='update_user'),
    path('<int:user_id>/delete/', delete_user, name='delete_user'),
]
