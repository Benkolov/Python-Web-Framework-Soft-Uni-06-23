from django.db import models
from django.contrib.auth import models as auth_models


class AppUser(auth_models.AbstractBaseUser):
    USERNAME_FIELD = 'email'

    # objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
