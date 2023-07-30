from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        Group, PermissionsMixin)
from django.contrib.gis.db import models

from utils.file_utils import user_directory_path


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email address is required")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("email_verified", True)
        kwargs.setdefault("is_active", True)
        return self.create_user(email=email, password=password, **kwargs)

    def create_staff_user(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", False)
        kwargs.setdefault("email_verified", True)
        kwargs.setdefault("is_active", True)
        return self.create_user(email=email, password=password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        blank=True,
        unique=True,
        db_index=True,
        verbose_name="email address",
        error_messages={
            "unique": "A user with that email address already exists.",
        },
    )
    is_staff = models.BooleanField(default=False)
    is_audience = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = "User"

    def save(self, *args, **kwargs):
        if self.is_staff and not self.is_superuser:
            group = Group.objects.get(name="staff")
            self.groups.add(group)
        super(User, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return " ".join([name for name in [self.first_name, self.last_name] if name])

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1024, default=None, null=True)
    profile_image = models.ImageField(
        default=None, null=True, upload_to=user_directory_path
    )

    def __str__(self):
        return self.user.email
