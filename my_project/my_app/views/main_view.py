from django.shortcuts import   render, redirect
from ..models import Todo
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    todos = Todo.objects.filter(user = request.user)
    return render(request, 'main/index.html', {'todos': todos})

@login_required
def create_todo(request):
    errors = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')

        if not title:
            errors['title'] = "Title is required"

        if not date:
            errors['date'] = "Date is required"



        if errors:
            return render(request, 'main/create_task.html', {
                'errors': errors,
                'data': request.POST
            })

        Todo.objects.create(
            title=title,  
            date=date,
            description=description,
            user=request.user
        )

        return redirect('index') 
    return render(request, 'main/create_task.html')
