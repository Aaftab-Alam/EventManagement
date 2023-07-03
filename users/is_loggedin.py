from django.shortcuts import render, redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.is_empty():
            return redirect('login_view')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper