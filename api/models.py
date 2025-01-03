from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=100)  # Who sent the message
    recipient = models.CharField(max_length=100)  # Who receives the message
    content = models.TextField()  # Message content
    timestamp = models.DateTimeField(auto_now_add=True)  # When the message was sent
    is_edited = models.BooleanField(default=False)  # Track if the message is edited

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.content[:30]}"

