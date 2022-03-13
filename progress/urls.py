from django.urls import path
from .views import *

urlpatterns = [
    path('course_progress', course_progress_tracking),
]
