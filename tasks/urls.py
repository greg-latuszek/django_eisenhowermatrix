from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="tasks-list"),
    path("update_task/<str:pk>/", views.update_task, name="update_task"),
]
