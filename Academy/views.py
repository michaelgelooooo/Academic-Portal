from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SupportChat, SupportMessage
from Students.models import Student
from Faculty.models import Faculty
from Parents.models import Parent


# Create your views here.
def index(request):
    return render(request, "academy/index.html")


def about(request):
    return render(request, "academy/about.html")


def get_user_info(user):
    if user.username.startswith("STU-"):
        user_info = Student.objects.get(student_id=user.username)
    elif user.username.startswith("FAC-"):
        user_info = Faculty.objects.get(faculty_id=user.username)
    elif user.username.startswith("PAR-"):
        user_info = Parent.objects.get(parent_id=user.username)

    return user_info


def chat(request):
    if not request.user.is_staff:
        messages.error(request, "Only staff accounts can access this page")
        return redirect("index")

    conversations = SupportChat.objects.all()

    for conversation in conversations:
        latest = SupportMessage.objects.filter(conversation=conversation).first()
        userinfo = get_user_info(conversation.chat_recipient)

        conversation.latest_message = latest
        conversation.user_info = userinfo

    context = {
        "conversations": conversations,
    }

    return render(request, "admin/chat.html", context)


def chat_view(request, pk):
    # Ensure only staff can access this page
    if not request.user.is_staff:
        messages.error(request, "Only staff accounts can access this page")
        return redirect("index")

    # Fetch the conversation
    conversation = get_object_or_404(SupportChat, pk=pk)
    user_info = get_user_info(conversation.chat_recipient)


    if request.method == "POST":
        # Get the message content and trim whitespace
        message_content = request.POST.get("message", "").strip()

        # Check if the message is valid (not empty after trimming)
        if message_content:
            # Create and save the new SupportMessage
            SupportMessage.objects.create(
                conversation=conversation,
                sender=request.user,
                content=message_content,
            )
            messages.success(request, "Message sent successfully!")
        else:
            # Handle empty or whitespace-only input
            messages.error(request, "Message cannot be empty or whitespace only.")


    # Fetch all chat messages for this conversation, ordered newest to oldest
    chats = SupportMessage.objects.filter(conversation=conversation)[::-1]

    context = {
        "chats": chats,
        "conversation": conversation,
        "user_info": user_info,
    }
    return render(request, "admin/chat_view.html", context)
