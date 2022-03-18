from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path("", views.index, name="tasks_list"),
    path("update_task/<str:pk>/", views.update_task, name="update_task"),
    path("delete/<str:pk>/", views.delete_task, name="delete_task"),
    path("prime/<int:x>/", views.show_primes, name="show_primes"),
]

# API
router = SimpleRouter()
router.register(r"tasks", views.TasksViewSet, "tasks")
