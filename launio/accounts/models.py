from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(2),
        )

    )

    email = models.EmailField(
    )

    birthdate = models.DateField()

    profile_image = models.URLField()


# # TEST
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.core.validators import MinLengthValidator
# from django.db import models
#
# from validators.image_validator import MaxFileSizeInMbValidator
#
# IMAGE_MAX_SIZE_IN_MB = 2
# MIN_NAMES_LENGTH_VALIDATOR = 2
#
#
# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password, first_name, last_name, username, **extra_fields):
#         if not email:
#             raise ValueError('Email not provided')
#         if not password:
#             raise ValueError('Password is not provided')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, first_name, last_name, username, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, first_name, last_name, username, **extra_fields)
#
#     def create_super_user(self,email, password, first_name, last_name, username, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, first_name, last_name, username, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, max_length=100)
#     username = models.CharField(validators=(
#         MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),), max_length=50)
#     first_name = models.CharField(validators=(
#         MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),), max_length=40)
#     last_name = models.CharField(validators=(
#         MinLengthValidator(MIN_NAMES_LENGTH_VALIDATOR),), max_length=40)
#     image = models.ImageField(
#         upload_to='users/',
#         null=True,
#         blank=True,
#         validators=(
#             MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
#         )
#     )
#
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'username', ]
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
