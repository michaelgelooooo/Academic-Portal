from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Announcements(models.Model):
    announcement_title = models.CharField(max_length=50)
    announcement_content = models.TextField()
    announcement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.announcement_date.strftime("%Y-%m-%d %H:%M:%S")

        return f"{self.announcement_title} Announced@{formatted_time}"

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
        ordering = ["announcement_date"]


class SupportChat(models.Model):
    chat_recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_recipient.username} Support Chat"

    class Meta:
        verbose_name = "Support Chat"
        verbose_name_plural = "Support Chats"
        ordering = ["-created_at"]


class SupportMessage(models.Model):
    conversation = models.ForeignKey(SupportChat, on_delete=models.CASCADE)

    def get_default_user():
        return User.objects.get(username="EduConnect")

    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sender_type = "Admin" if self.sender.is_staff else self.sender.username
        return f"Message from {sender_type} @{self.timestamp}"

    class Meta:
        verbose_name = "Support Message"
        verbose_name_plural = "Support Messages"
        ordering = ["-timestamp"]


class UserAccessLogs(models.Model):
    user_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.user_name} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "User Access Log"
        verbose_name_plural = "User Access Logs"


class UserAccountLogs(models.Model):
    user_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.user_name} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "User Account Log"
        verbose_name_plural = "User Account Logs"


class SubjectsChangesLogs(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.subject_code} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "Subjects Changes Log"
        verbose_name_plural = "Subjects Changes Logs"


class ClassChangesLogs(models.Model):
    class_name = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.class_name} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "Class Changes Log"
        verbose_name_plural = "Class Changes Logs"


class LectureMaterialsLogs(models.Model):
    material_id = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.material_id} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "Lecture Materials Log"
        verbose_name_plural = "Lecture Materials Logs"


class GradeChangesLogs(models.Model):
    student_id = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.student_id} - {self.subject_code} Updated@{formatted_time}"

    class Meta:
        verbose_name = "Grade Changes Log"
        verbose_name_plural = "Grade Changes Logs"


class TaskChangesLog(models.Model):
    task_id = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.task_id} {self.action}@{formatted_time}"

    class Meta:
        verbose_name = "Task Changes Log"
        verbose_name_plural = "Task Changes Logs"
