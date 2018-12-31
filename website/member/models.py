from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(
        max_length=256, unique=True)
    name = models.CharField(max_length=50, blank=True)
    phone_num = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=1028, blank=True)
    homepage = models.URLField(blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [

    ]

    objects = MyUserManager()

    def __str__(self):
        return '{},{},{},{},{}'.format(
            self.username,
            self.name,
            self.phone_num,
            self.address,
            self.homepage,
        )
