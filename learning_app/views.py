from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import todo
from .form import CreateTodoForm
from django.http import FileResponse
from django.contrib.auth.decorators import login_required


def pdf_view(request, pk):
    todo_item = get_object_or_404(todo, pk=pk)
    response = FileResponse(todo_item.pdf_file.open(), content_type='application/pdf')
    return response


def todo_detail(request, pk):
    todo_item = get_object_or_404(todo, pk=pk)
    context = {'todo_item': todo_item}
    return render(request, 'learning_app/todo_detail.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST, request.FILES)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'Todo item added')
            return redirect('all-todos')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('create-todo')
    else:
        form = CreateTodoForm()
        context = {'form': form}
        return render(request, 'learning_app/create_todo.html', context)


# added 2 roles

@login_required
def all_todos(request):
    if request.user.role == 'creator':
        obj = todo.objects.filter(user=request.user)
    elif request.user.role == 'reviewer':
        # Adjust the query based on your logic for reviewers
        obj = todo.objects.all()
    else:
        # Handle other roles or unexpected scenarios
        obj = todo.objects.none()

    context = {'obj': obj}
    return render(request, 'learning_app/all_todos.html', context)


