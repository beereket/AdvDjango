from django.urls import path
from . import views

urlpatterns = [
    # Пример URL для загрузки резюме
    path('upload/', views.UploadResumeView.as_view(), name='upload-resume'),
    # Пример URL для получения резюме
    path('resume/<int:id>/', views.ResumeDetailView.as_view(), name='resume-detail'),
]
