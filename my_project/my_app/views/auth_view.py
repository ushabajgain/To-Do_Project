from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    errors = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email) # select * from User where email=email
            auth_user = authenticate(request, username=user.username, password=password)
            print(auth_user.username)

            if auth_user is not None:
                login(request, auth_user) # session generate garxa
                return redirect('index')
            else:
                errors['login_error'] = "Invalid email or password"
        except User.DoesNotExist:
            errors['login_error'] = "User with this email does not exist"

        return render(request, 'auth/login_page.html', {'errors': errors})

    return render(request, 'auth/login_page.html')


def register_page(request):
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username:
           errors['username'] = "Username field is required"

        if not email:
            errors['email'] = "Email field is required"

        if not password:
            errors['password'] = "Password field is required"

        if not confirm_password:
            errors['confirm_password'] = "Confirm password field is required"

        if password and confirm_password and password != confirm_password:
            errors['confirm_password'] = "Password and confirm password do not match"


        if not errors:
            # user = User.objects.create(
            #     username=username,
            #     email=email
            # )
            # user.set_password(password)
            # user.save()
            
            user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')

    else:
            return render(request, 'auth/register_page.html', {'errors': errors, 'data': request.POST})



def logout_user(request):
    logout(request)
    return redirect('index')
