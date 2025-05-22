from django.db import models

# Create your models here.


class dbteacher1(models.Model):
    t_id=models.AutoField(primary_key=True)
    t_email=models.EmailField(unique=True)
    t_password=models.CharField(max_length=50)
    def __str__(self):
        return self.t_email
    
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class dbstudent1(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    s_id = models.AutoField(primary_key=True)
    s_profilepicture = models.ImageField(upload_to='profilepics/', blank=True, null=True)
    s_firstname = models.CharField(max_length=50)
    s_lastname = models.CharField(max_length=50)
    s_email = models.EmailField(unique=True)
    s_phonenumber = models.BigIntegerField()
    s_guardianphonenumber = models.BigIntegerField()
    s_qualification = models.TextField()
    s_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    s_password = models.CharField(max_length=128, blank=True)

    def save(self, *args, **kwargs):
        if self.s_password and not self.s_password.startswith('pbkdf2_'):
            self.s_password = make_password(self.s_password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.s_password)

    def __str__(self):
        return self.s_email
