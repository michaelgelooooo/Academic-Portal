from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver


class Student(models.Model):
    student_id = models.CharField(max_length=8, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

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