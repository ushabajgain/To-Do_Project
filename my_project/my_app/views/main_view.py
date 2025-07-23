from django.shortcuts import  get_object_or_404, render, redirect
from ..models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user)
    priority_filter = request.GET.get('priority')
    sort_by = request.GET.get('sort')
    if priority_filter in ['low', 'medium', 'high']:
        todos = todos.filter(priority=priority_filter)
    if sort_by == 'priority':
        todos = todos.order_by('priority', 'date')
    elif sort_by == 'priority_desc':
        todos = todos.order_by('-priority', 'date')
    elif sort_by == 'date':
        todos = todos.order_by('date')
    elif sort_by == 'date_desc':
        todos = todos.order_by('-date')
    return render(request, 'main/index.html', {
        'todos': todos,
        'priority_filter': priority_filter,
        'sort_by': sort_by
    })

@login_required
def create_todo(request):
    from ..models import Category
    errors = {}

    categories = Category.objects.filter(is_predefined=True) | Category.objects.filter(user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        category_name = request.POST.get('category_name', '').strip()
        priority = request.POST.get('priority', 'medium')

        if not title:
            errors['title'] = "Title is required"

        if not date:
            errors['date'] = "Date is required"

        category = None
        if category_name:
            category = Category.objects.filter(name__iexact=category_name).filter(models.Q(is_predefined=True) | models.Q(user=request.user)).first()
            if not category:
                category = Category.objects.create(
                    name=category_name,
                    user=request.user,
                    is_predefined=False
                )
        elif category_name == '':
            category = None

        if errors:
            return render(request, 'main/create_task.html', {
                'errors': errors,
                'data': request.POST,
                'categories': categories
            })

        Todo.objects.create(
            title=title,  
            date=date,
            description=description,
            user=request.user,
            category=category,
            priority=priority
        )

        return redirect('index') 
    return render(request, 'main/create_task.html', {'categories': categories})


def edit_todo(request, id):
    from ..models import Category
    previous_data = Todo.objects.get(id=id) 
    categories = Category.objects.filter(is_predefined=True) | Category.objects.filter(user=request.user)
    print(previous_data.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        category_name = request.POST.get('category_name', '').strip()
        priority = request.POST.get('priority', 'medium')
        
        errors = {}
        
        if not title:
            errors['title'] = "Title is required"
            
        if not date:
            errors['date'] = "Date is required"

        if not description:
            errors['description'] = "Description is required"    
        
        category = previous_data.category
        if category_name:
            category = Category.objects.filter(name__iexact=category_name).filter(models.Q(is_predefined=True) | models.Q(user=request.user)).first()
            if not category:
                category = Category.objects.create(
                    name=category_name,
                    user=request.user,
                    is_predefined=False
                )
        elif category_name == '':
            category = None
        
        if previous_data.user == request.user:
            if errors:
                return render(request,'main/edit_task.html',{'todo':previous_data, 'errors':errors, 'categories': categories})
            
            previous_data.title = title
            previous_data.date = date
            previous_data.description = description
            previous_data.category = category
            previous_data.priority = priority
            previous_data.save()
            return redirect('index') 
        else:
            messages.error(request,'You are not authorized to edit this task.')
                
    return render(request,'main/edit_task.html',{'todo':previous_data, 'categories': categories})


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


@login_required
def profile_page(request):
    user = request.user
    errors = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not email:
            errors['email'] = 'Email is required'
        if not username:
            errors['username'] = 'Username is required'
        if errors:
            return render(request, 'main/profile_page.html', {'user': user, 'errors': errors})

        try:
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        except Exception as e:
            messages.error(request, f"Failed to update profile! {e}")
            return redirect('profile')
    return render(request, 'main/profile_page.html', {'user': user})

