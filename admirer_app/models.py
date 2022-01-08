from django.db import models

# Create your models here.

class Secret_Messages(models.Model):
    recipient = models.CharField(max_length=15)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f"{self.recipient} + {self.date}"

    def save(self, *args, **kwargs):
        self.recipient = self.recipient.lower()
        return super(Secret_Messages, self).save(*args, **kwargs)
    