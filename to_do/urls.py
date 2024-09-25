from django.urls import path

from to_do.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, toggle_task_is_done,
)

app_name = "to_do"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="home-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="home-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="home-delete"),
    path(
        "<int:pk>/toggle-is-done/",
        toggle_task_is_done,
        name="toggle-task-is-done",
    ),

    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tags-delete"),
]
