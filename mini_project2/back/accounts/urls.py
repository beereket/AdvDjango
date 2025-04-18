from django.urls import path
from . import views

urlpatterns = [
    # Пример URL для просмотра пользователя (вы можете добавить другие необходимые URL)
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
]
