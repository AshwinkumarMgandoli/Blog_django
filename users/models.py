from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Save the profile first
        super().save(*args, **kwargs)

        # Check if the image exists before opening it
        try:
            img = Image.open(self.image.path)
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            # For example, you can set a default image if the file is missing
            self.image = 'default.jpg'
            super().save(*args, **kwargs)
            return  # Exit to prevent further processing

        # Resize image if it's too large
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

