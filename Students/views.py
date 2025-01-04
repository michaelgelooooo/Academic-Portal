from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm


# Create your views here.
@login_required(login_url="student-login")
def dashboard(request):
    context = {"student_id": request.user.username}

    return render(request, "students/dashboard.html", context)

@login_required(login_url="student-login")
def profile(request):
    context = {"student_id": request.user.username}

    return render(request, "students/profile.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect('student-dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get('student_id')
            password = form.cleaned_data.get('password')
            user = authenticate(username=student_id, password=password)
            
            if user is not None:
                if not user.username.startswith('STU-'):
                    messages.error(request, 'Only student accounts can login here')
                else:
                    auth_login(request, user)
                    return redirect('student-dashboard')
            else:
                messages.error(request, 'Invalid student ID or password')
    else:
        form = LoginForm()
    
    context = {"form": form}
    
    return render(request, "students/login.html", context)
