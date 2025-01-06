from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from datetime import datetime
from Academy.models import UserAccountLogs
import os


def profile_pic_path(instance, filename):
    ext = filename.split(".")[-1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"profile_pictures/parents/{instance.parent_id}_{timestamp}.{ext}"


class Parent(models.Model):
    parent_id = models.CharField(max_length=8, unique=True, blank=True)
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
                old_instance = Parent.objects.get(pk=self.pk)
                # Check if password was changed
                if old_instance.password != self.password:
                    # Update Django User password
                    try:
                        user = User.objects.get(username=self.parent_id)
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
            except Parent.DoesNotExist:
                pass
                
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent_id} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"


@receiver(pre_save, sender=Parent)
def generate_parent_id(sender, instance, **kwargs):
    if not instance.parent_id:
        # Get last parent record
        last_parent = Parent.objects.order_by("-parent_id").first()

        if last_parent:
            # Extract number from last ID and increment
            last_number = int(last_parent.parent_id.split("-")[1])
            new_number = last_number + 1
        else:
            new_number = 1

        # Format new parent ID
        instance.parent_id = f"PAR-{new_number:04d}"


@receiver(post_save, sender=Parent)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.parent_id,
            password=instance.password,
        )

        UserAccountLogs.objects.create(
            user_name=instance.parent_id, user_type="Parent", action="Created"
        )
    else:
        # Log the update action
        UserAccountLogs.objects.create(
            user_name=instance.parent_id, user_type="Parent", action="Updated"
        )


@receiver(pre_delete, sender=Parent)
def delete_user_account(sender, instance, **kwargs):
    """Delete the associated User when a Parent is deleted"""
    try:
        # Add a flag to the instance to prevent recursive deletion
        if not hasattr(instance, "_user_being_deleted"):
            user = User.objects.get(username=instance.parent_id)
            # Set flag on user to prevent recursive deletion
            user._parent_being_deleted = True

            UserAccountLogs.objects.create(
                user_name=instance.parent_id, user_type="Parent", action="Deleted"
            )

            user.delete()
    except User.DoesNotExist:
        pass


@receiver(pre_delete, sender=User)
def delete_parent_record(sender, instance, **kwargs):
    """Delete the associated Parent when a User is deleted"""
    try:
        # Only delete the parent if this deletion didn't come from the parent deletion
        if not hasattr(instance, "_parent_being_deleted"):
            parent = Parent.objects.get(parent_id=instance.username)
            # Set flag on parent to prevent recursive deletion
            parent._user_being_deleted = True

            UserAccountLogs.objects.create(
                user_name=instance.username, user_type="Parent", action="Deleted"
            )

            parent.delete()
    except Parent.DoesNotExist:
        pass