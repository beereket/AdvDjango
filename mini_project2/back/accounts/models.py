from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='job_seeker')

    # Добавляем параметр related_name для разрешения конфликтов
    groups = models.ManyToManyField(
        Group, 
        related_name='accounts_user_set',  # Это позволяет избежать конфликта с auth.User
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_user_permissions_set',  # Это позволяет избежать конфликта с auth.User
        blank=True
    )
