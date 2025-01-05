from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import LoginForm, EditProfileForm
from .models import Faculty
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
def schedule(request):
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
