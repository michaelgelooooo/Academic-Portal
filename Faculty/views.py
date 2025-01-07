from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib import messages
from .forms import LoginForm, EditProfileForm
from .models import Faculty, Subjects
from Academy.models import UserAccessLogs
from datetime import datetime, timedelta
from PIL import Image
from io import BytesIO
import sys
import logging
from django.core.files.uploadedfile import InMemoryUploadedFile


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
        "profile_pic": faculty.profile_pic,
    }

    return render(request, "faculty/dashboard.html", context)


@login_required(login_url="faculty-login")
def subjects(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")

    faculty = Faculty.objects.get(faculty_id=request.user.username)
    subjects = Subjects.objects.filter(instructor=faculty)

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "profile_pic": faculty.profile_pic,
        "subjects": subjects,
    }

    return render(request, "faculty/subjects.html", context)


@login_required(login_url="faculty-login")
def subject_view(request, subject_code):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty = Faculty.objects.get(faculty_id=request.user.username)
    subject = Subjects.objects.get(subject_code=subject_code)

    subject.formatted_schedule = f"{subject.schedule.strftime('%I:%M %p')}"

    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "profile_pic": faculty.profile_pic,
        "subject": subject,
    }

    return render(request, "faculty/subject_view.html", context)


@login_required(login_url="faculty-login")
def schedule(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")

    faculty = Faculty.objects.get(faculty_id=request.user.username)
    subjects = Subjects.objects.filter(instructor=faculty).order_by("schedule")

    for subject in subjects:
        # Convert time to datetime for calculation
        start_datetime = datetime.combine(datetime.today(), subject.schedule)
        end_datetime = start_datetime + timedelta(hours=1)
        
        # Format using the time component
        subject.formatted_schedule = f"{start_datetime.strftime('%I:%M %p')} - {end_datetime.strftime('%I:%M %p')}"
    
    context = {
        "faculty_id": faculty.faculty_id,
        "first_name": faculty.first_name,
        "last_name": faculty.last_name,
        "profile_pic": faculty.profile_pic,
        "subjects": subjects,
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
        "profile_pic": faculty.profile_pic,
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
        "profile_pic": faculty.profile_pic,
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
        "profile_pic": faculty.profile_pic,
    }

    return render(request, "faculty/edit_profile.html", context)


logger = logging.getLogger(__name__)


def crop_square_image(image):
    try:
        # Convert to RGB if needed
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Get dimensions
        width, height = image.size
        crop_size = min(width, height)

        # Center crop
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        image = image.crop((left, top, right, bottom))
        image = image.resize((300, 300), Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        logger.error(f"Image processing error: {str(e)}")
        return None


@login_required(login_url="faculty-login")
def update_profile_pic(request):
    try:
        if not request.user.username.startswith("FAC-"):
            messages.error(request, "Only faculty accounts can access this page")
            return redirect("faculty-login")

        if request.method == "POST" and request.FILES.get("profile_pic"):
            faculty = Faculty.objects.get(faculty_id=request.user.username)
            upload = request.FILES["profile_pic"]

            # Validate file
            if not upload.content_type.startswith("image"):
                messages.error(request, "Please upload a valid image file")
                return redirect("faculty-profile")

            # Process image
            img = Image.open(upload)
            processed_img = crop_square_image(img)

            if processed_img:
                # Save processed image
                output = BytesIO()
                processed_img.save(output, format="JPEG", quality=90)
                output.seek(0)

                # Create new file
                processed_file = InMemoryUploadedFile(
                    output,
                    "ImageField",
                    f"{upload.name.split('.')[0]}.jpg",
                    "image/jpeg",
                    sys.getsizeof(output),
                    None,
                )

                faculty.profile_pic = processed_file
                faculty.save()
                messages.success(request, "Profile picture updated successfully!")
            else:
                messages.error(request, "Error processing image")
        else:
            messages.error(request, "No image file provided")

        return redirect("faculty-profile")

    except Exception as e:
        logger.error(f"Profile pic update error: {str(e)}")
        messages.error(request, "Error updating profile picture")
        return redirect("faculty-profile")


@login_required(login_url="faculty-login")
def update_password(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("faculty-profile")

        if len(new_password) < 8:
            messages.error(request, "Password must be at least 8 characters long")
            return redirect("faculty-profile")

        try:
            # Get both Faculty and User instances
            faculty = Faculty.objects.get(faculty_id=request.user.username)
            user = request.user

            # Update password in both models
            faculty.password = new_password
            user.set_password(new_password)

            # Save both models
            faculty.save()
            user.save()

            # Update session auth hash AFTER saving
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated successfully!")

        except Exception as e:
            logger.error(f"Password update error: {str(e)}")
            messages.error(request, "Error updating password")

    return redirect("faculty-profile")


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

                    # Create log entry after successful login
                    UserAccessLogs.objects.create(
                        user_name=faculty_id, user_type="Faculty", action="Login"
                    )

                    return redirect("faculty-dashboard")
            else:
                messages.error(request, "Invalid faculty ID or password")
    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "faculty/login.html", context)


@login_required(login_url="faculty-login")
def logout(request):
    if not request.user.username.startswith("FAC-"):
        messages.error(request, "Only faculty accounts can access this page")
        return redirect("faculty-login")
    
    faculty_id = request.user.username
    
    if request.method == "POST":
        auth_logout(request)

        UserAccessLogs.objects.create(
            user_name=faculty_id, user_type="Faculty", action="Logout"
        )

    return redirect("faculty-login")