from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm, EditProfileForm
from .models import Parent


# Create your views here.
@login_required(login_url="parent-login")
def dashboard(request):
    if not request.user.username.startswith("PAR-"):
        messages.error(request, "Only parent accounts can access this page")
        return redirect("parent-login")
    
    parent = Parent.objects.get(parent_id=request.user.username)

    context = {
        "parent_id": parent.parent_id,
        "first_name": parent.first_name,
        "last_name": parent.last_name,
    }

    return render(request, "parents/dashboard.html", context)


@login_required(login_url="parent-login")
def family(request):
    if not request.user.username.startswith("PAR-"):
        messages.error(request, "Only parent accounts can access this page")
        return redirect("parent-login")
    
    parent = Parent.objects.get(parent_id=request.user.username)

    context = {
        "parent_id": parent.parent_id,
        "first_name": parent.first_name,
        "last_name": parent.last_name,
    }

    return render(request, "parents/family.html", context)


@login_required(login_url="parent-login")
def chat(request):
    if not request.user.username.startswith("PAR-"):
        messages.error(request, "Only parent accounts can access this page")
        return redirect("parent-login")
    
    parent = Parent.objects.get(parent_id=request.user.username)

    context = {
        "parent_id": parent.parent_id,
        "first_name": parent.first_name,
        "last_name": parent.last_name,
    }

    return render(request, "parents/chat.html", context)


@login_required(login_url="parent-login")
def profile(request):
    if not request.user.username.startswith("PAR-"):
        messages.error(request, "Only parent accounts can access this page")
        return redirect("parent-login")
    
    parent = Parent.objects.get(parent_id=request.user.username)

    context = {
        "parent_id": parent.parent_id,
        "first_name": parent.first_name,
        "last_name": parent.last_name,
        "email": parent.email,
        "phone_number": parent.phone_number,
    }

    return render(request, "parents/profile.html", context)

@login_required(login_url="parent-login")
def edit_profile(request):
    if not request.user.username.startswith("PAR-"):
        messages.error(request, "Only parent accounts can access this page")
        return redirect("parent-login")
    
    parent = Parent.objects.get(parent_id=request.user.username)
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("parent-profile")
    else:
        form = EditProfileForm(instance=parent)
    
    context = {
        "form": form,
        "parent_id": parent.parent_id,
        "first_name": parent.first_name,
        "last_name": parent.last_name,
    }
    
    return render(request, "parents/edit_profile.html", context)

def login(request):
    if request.user.is_authenticated and request.user.username.startswith("PAR-"):
        return redirect("parent-dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            parent_id = form.cleaned_data.get("parent_id")
            password = form.cleaned_data.get("password")
            user = authenticate(username=parent_id, password=password)

            if user is not None:
                if not user.username.startswith("PAR-"):
                    messages.error(request, "Only parent accounts can login here")
                else:
                    auth_login(request, user)
                    return redirect("parent-dashboard")
            else:
                messages.error(request, "Invalid parent ID or password")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "parents/login.html", context)
