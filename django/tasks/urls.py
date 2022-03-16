from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"tasks", views.TasksViewSet, "tasks")

urlpatterns = [
    path("", views.index, name="tasks_list"),
    path("update_task/<str:pk>/", views.update_task, name="update_task"),
    path("delete/<str:pk>/", views.delete_task, name="delete_task"),
    path("prime/<int:x>/", views.show_primes, name="show_primes"),
    path("api/", include(router.urls))
]
