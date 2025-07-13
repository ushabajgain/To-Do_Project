from django.shortcuts import  get_object_or_404, render, redirect
from ..models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


def edit_todo(request, id):
    previous_data = Todo.objects.get(id=id) 
    print(previous_data.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        errors = {}
        
        if not title:
            errors['title'] = "Title is required"
            
        if not date:
            errors['date'] = "Date is required"

        if not description:
            errors['description'] = "Description is required"    
        
        if previous_data.user == request.user:
            if errors:
                return render(request,'main/edit_task.html',{'todo':previous_data, 'errors':errors})
            
            previous_data.title = title
            previous_data.date = date
            previous_data.description = description
            previous_data.save()
            return redirect('index') 
        else:
            messages.error(request,'You are not authorized to edit this task.')
                
    return render(request,'main/edit_task.html',{'todo':previous_data})


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    
    if todo.user == request.user:
        todo.delete()
        messages.success(request, "Todo deleted successfully.")
        return redirect('index')
    else:
        messages.error(request, "You are not authorized to delete this task.")
        return redirect('index')


    
