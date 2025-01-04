from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm, EditProfileForm
from .models import Student


# Create your views here.
@login_required(login_url="student-login")
def dashboard(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return render(request, "students/dashboard.html", context)


@login_required(login_url="student-login")
def subjects(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return render(request, "students/subjects.html", context)


@login_required(login_url="student-login")
def schedule(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return render(request, "students/schedule.html", context)


@login_required(login_url="student-login")
def grades(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }
    return render(request, "students/grades.html", context)


@login_required(login_url="student-login")
def chat(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }

    return render(request, "students/chat.html", context)


@login_required(login_url="student-login")
def profile(request):
    student = Student.objects.get(student_id=request.user.username)

    context = {
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "email": student.email,
        "phone_number": student.phone_number,
    }

    return render(request, "students/profile.html", context)

@login_required(login_url="student-login")
def edit_profile(request):
    student = Student.objects.get(student_id=request.user.username)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("student-profile")
    else:
        form = EditProfileForm(instance=student)
    
    context = {
        "form": form,
        "student_id": student.student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
    }
    
    return render(request, "students/edit_profile.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect("student-dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data.get("student_id")
            password = form.cleaned_data.get("password")
            user = authenticate(username=student_id, password=password)

            if user is not None:
                if not user.username.startswith("STU-"):
                    messages.error(request, "Only student accounts can login here")
                else:
                    auth_login(request, user)
                    return redirect("student-dashboard")
            else:
                messages.error(request, "Invalid student ID or password")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "students/login.html", context)
