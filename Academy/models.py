from django.db import models


# Create your models here.
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
