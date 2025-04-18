from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from resumes.models import Resume, ResumeFeedback
from .serializers import ResumeSerializer, ResumeFeedbackSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ResumeFeedback.objects.all()
    serializer_class = ResumeFeedbackSerializer
