from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="tasks_list"),
    path("update_task/<str:pk>/", views.update_task, name="update_task"),
    path("delete/<str:pk>/", views.delete_task, name="delete_task"),
    path("prime/<int:x>/", views.show_primes, name="show_primes"),
    path("api/list_tasks/", views.list_tasks, name="api_list_tasks"),
]
