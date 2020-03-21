from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model for authentication"""
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField("Email", max_length=255, unique=True)
    mobile = models.CharField("Mobile", max_length=17, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return 'User: ' + self.username

class Profile(models.Model):
    """Profile model for user, contains user profile details"""
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    user = models.OneToOneField("User", on_delete=models.CASCADE, primary_key=True, related_name="User")
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    gender = models.CharField("Gender", max_length=10, choices=GENDER)
    dob = models.DateField("DOB", blank=True, null=True)
    friends = models.ManyToManyField("User", related_name="friends_list", blank=True)
    joined = models.DateTimeField("Joined", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)

    def delete(self, *args, **kwargs):
        """Deletes the user object if the profile object for the user have been deleted"""
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return 'Profile: '+self.first_name +' '+self.last_name+' ('+self.user.username +')'
