from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver


class Parent(models.Model):
    parent_id = models.CharField(max_length=8, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.parent_id} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parent"


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


@receiver(pre_delete, sender=Parent)
def delete_user_account(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.parent_id)
        user.delete()
    except User.DoesNotExist:
        pass