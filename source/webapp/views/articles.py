from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import ToDoList


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_task.html')
    print(request.POST)
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status', 'new'),
        'due_date': request.POST.get('due_date')
    }
    task = ToDoList.objects.create(**task_data)
    return redirect(f'/task/?pk={task.pk}')


def edit_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        try:
            task.set_status(new_status)
        except ValueError as e:
            context = {'task': task, 'status_choices': ToDoList.STATUS_CHOICES, 'error_message': str(e)}
            return render(request, 'edit_task.html', context=context)

        return redirect(f'/task/?pk={task.pk}')

    context = {'task': task, 'status_choices': ToDoList.STATUS_CHOICES}
    return render(request, 'edit_task.html', context=context)

def detail_view(request):
    task_pk = request.GET.get('pk')
    task = ToDoList.objects.get(pk=task_pk)
    context = {
        'task': task
    }
    return render(request, 'task.html', context=context)
