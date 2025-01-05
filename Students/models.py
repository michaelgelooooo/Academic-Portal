from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from datetime import datetime
import os


def profile_pic_path(instance, filename):
    ext = filename.split(".")[-1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"profile_pictures/students/{instance.student_id}_{timestamp}.{ext}"


class Student(models.Model):
    student_id = models.CharField(max_length=8, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(
        upload_to=profile_pic_path,
        default="profile_pictures/blank.jpg",
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Handle profile picture changes
        if self.pk:
            try:
                old_instance = Student.objects.get(pk=self.pk)
                # Check if password was changed
                if old_instance.password != self.password:
                    # Update Django User password
                    try:
                        user = User.objects.get(username=self.student_id)
                        user.set_password(self.password)
                        user.save()
                    except User.DoesNotExist:
                        pass
                        
                # Existing profile pic handling
                if old_instance.profile_pic != self.profile_pic:
                    if os.path.exists(
                        old_instance.profile_pic.path
                    ) and not old_instance.profile_pic.path.endswith("blank.jpg"):
                        os.remove(old_instance.profile_pic.path)
            except Student.DoesNotExist:
                pass
                
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


@receiver(pre_save, sender=Student)
def generate_student_id(sender, instance, **kwargs):
    if not instance.student_id:
        # Get last student record
        last_student = Student.objects.order_by("-student_id").first()

        if last_student:
            # Extract number from last ID and increment
            last_number = int(last_student.student_id.split("-")[1])
            new_number = last_number + 1
        else:
            new_number = 1

        # Format new student ID
        instance.student_id = f"STU-{new_number:04d}"


@receiver(post_save, sender=Student)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.student_id,
            password=instance.password,
        )


@receiver(pre_delete, sender=Student)
def delete_user_account(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.student_id)
        user.delete()
    except User.DoesNotExist:
        pass
