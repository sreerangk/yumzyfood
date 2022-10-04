from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    pass


class UserManager(AbstractBaseUser):
    pass