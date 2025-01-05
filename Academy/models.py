from django.db import models


# Create your models here.
class UserAccessLogs(models.Model):
    user_id = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    log_type = models.CharField(max_length=50)
    log_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.log_time.strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.user_id} {self.log_type}@{formatted_time}"

    class Meta:
        verbose_name = "User Access Log"
        verbose_name_plural = "User Access Logs"
