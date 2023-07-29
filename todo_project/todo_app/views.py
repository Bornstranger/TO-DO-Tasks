from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todo_items': todo_items})

def add_todo_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        TodoItem.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo_app/add_todo_item.html')

def update_todo_item(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        completed = 'completed' in request.POST
        todo_item.title = title
        todo_item.description = description
        todo_item.completed = completed
        todo_item.save()
        return redirect('todo_list')

    return render(request, 'todo_app/update_todo_item.html', {'todo_item': todo_item})

def delete_todo_item(request, pk):
    todo_item = get_object_or_404(TodoItem, pk=pk)

    if request.method == 'POST':
        todo_item.delete()
        return redirect('todo_list')

    return render(request, 'todo_app/delete_todo_item.html', {'todo_item': todo_item})
