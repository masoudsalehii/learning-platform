from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    progress = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

