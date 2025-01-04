from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm, EditProfileForm
from .models import Faculty


# Create your views here.
@login_required(login_url="faculty-login")
def dashboard(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
    }

    return render(request, "faculty/dashboard.html", context)


@login_required(login_url="faculty-login")
def schedule(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
    }

    return render(request, "faculty/schedule.html", context)


@login_required(login_url="faculty-login")
def chat(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
    }

    return render(request, "faculty/chat.html", context)


@login_required(login_url="faculty-login")
def profile(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "email": faculty.email,
        "phone_number": faculty.phone_number,
    }

    return render(request, "faculty/profile.html", context)

@login_required(login_url="faculty-login")
def edit_profile(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("faculty-profile")
    else:
        form = EditProfileForm(instance=faculty)
    
    context = {
        "form": form,
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
    }
    
    return render(request, "faculty/edit_profile.html", context)

def login(request):
    if request.user.is_authenticated and request.user.username.startswith("FAC-"):
        return redirect("faculty-dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            faculty_id = form.cleaned_data.get("faculty_id")
            password = form.cleaned_data.get("password")
            user = authenticate(username=faculty_id, password=password)

            if user is not None:
                if not user.username.startswith("FAC-"):
                    messages.error(request, "Only faculty accounts can login here")
                else:
                    auth_login(request, user)
                    return redirect("faculty-dashboard")
            else:
                messages.error(request, "Invalid faculty ID or password")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "faculty/login.html", context)
