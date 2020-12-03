from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address.'))
        if not user_name:
            raise ValueError(_('You must provide a user name.'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        if not email:
            raise ValueError(_('You must provide an email address.'))
        if not user_name:
            raise ValueError(_('You must provide a user name.'))

        return self.create_user(email, user_name, password, **other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email                   = models.EmailField(_('Email Address'), unique=True)
    user_name               = models.CharField(_('User Name'), max_length=150, unique=True)
    first_name              = models.CharField(_('First Name'), max_length=150, null=True, blank=True)
    last_name               = models.CharField(_('Last Name'), max_length=150, null=True, blank=True)
    join_date               = models.DateTimeField(_('Join Date'), auto_now_add=True)
    last_login              = models.DateTimeField(_('Last Login'), auto_now=True)
    about                   = models.TextField(_('About'), max_length=500, blank=True, null=True)
    tagline                 = models.TextField(_('Tag Line'), max_length=50, null=True, blank=True)
    website                 = models.URLField(_('website'), max_length=100, null=True, blank=True)
    privacy_email           = models.BooleanField(_('Hide Email Address?'), default=True)
    privacy_library         = models.BooleanField(_('Hide Library?'), default=False)
    profile_image           = models.ImageField(_('Profile Image'), max_length=255, null=True, blank=True)
    profile_background      = models.ImageField(_('Profile Background'), max_length=255, null=True, blank=True)
    
    is_staff                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_admin                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD          = 'email'
    REQUIRED_FIELDS         = ['user_name',]

    objects                 = CustomUserManager()

    def __str__(self):
        return self.user_name