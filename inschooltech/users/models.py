from config.basemodels import BaseModel
from django.contrib.auth.models import AbstractUser


class User(BaseModel, AbstractUser):
    pass
