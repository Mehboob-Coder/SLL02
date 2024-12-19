import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email=models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    file=models.FileField(upload_to='files', blank=True)
    Reg_id = models.UUIDField( default=uuid.uuid4 ,unique=True , editable=False)

    def save(self, *args, **kwargs):
            if not self.Reg_id:
                self.Reg_id = uuid.uuid4()
            super().save(*args, **kwargs)


