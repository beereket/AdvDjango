from django.db import models
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    parsed_data = models.JSONField(default=dict)  # Для хранения данных, полученных из анализа
    created_at = models.DateTimeField(auto_now_add=True)

class ResumeFeedback(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
