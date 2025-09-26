from django.urls import path
from schoolapp import views

urlpatterns = [
    path("", views.student1, name="student"),
]
