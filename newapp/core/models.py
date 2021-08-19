from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
import uuid

# Create your models here.


def image_name_change(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return 'media_in/'+filename
    

# Changing the default authentication
# ? https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#auth-custom-user


class UserProfileManager(BaseUserManager):
    """Manager of User Profile"""

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError("User must have an email address")

# ? https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email

        # Normalizes email addresses by lowercasing the domain portion of the email address.
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  # to ensure encrypt password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Databse model for users in the system"""
    email = models.EmailField(
        max_length=150, unique=True, null=False, blank=False)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string reperesentation of our user"""
        return self.email

    class Meta:
        # this used to change the model name that appear in admin page
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles Plural"  # change model name in Admin panel


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        'UserProfile',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=image_name_change)
    created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'dbo.ProfileFeedItem'


