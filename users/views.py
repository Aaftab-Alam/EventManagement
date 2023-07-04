from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Users


def register(request):
    request.session.flush()
    if request.method == 'POST':
        print(request.session.is_empty())
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = Users(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],

            )
            user.save()
            request.session['id']=str(user._id)
            request.session['email'] = user.email
            request.session['username'] = user.username

            print(request.session.is_empty())

            return redirect('display_events')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    print(request.session.is_empty())
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Users.objects.filter(email=email).first()
            if user is not None and user.password==password:
                request.session['id']=str(user._id)
                print(request.session.get('id'))
                request.session['email'] = user.email
                request.session['username'] = user.username
                return redirect('display_events')
            else:
                error_message = 'Invalid username or password'
                print(error_message)
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
        else:
            print("Invalid form")
    else:

        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    return redirect('login_view')
