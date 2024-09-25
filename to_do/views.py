from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do.forms import TaskForm
from to_do.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do/home.html"

    def get_queryset(self):
        return Task.objects.prefetch_related('tags').all()


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:home")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:home")

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.delete()
        return redirect(self.success_url)


def toggle_task_is_done(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()

    return redirect(reverse_lazy("to_do:home"))


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "to_do/tags.html"


class TagCreateView(CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("to_do:tags")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("to_do:tags")


class TagDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:tags")

    def post(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs["pk"])
        tag.delete()
        return redirect(self.success_url)
