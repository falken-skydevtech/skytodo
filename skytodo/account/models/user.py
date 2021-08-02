from django.db import models
import json
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AppUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class AppUser(AbstractBaseUser):

    objects = AppUserManager()

    email   = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def initialize_create_account(self):
        from application.models import initialize_create_account
        initialize_create_account(self)
