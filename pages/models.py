from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)