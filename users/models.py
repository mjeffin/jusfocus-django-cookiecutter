from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    phone = CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$')])
    REQUIRED_FIELDS = ["name", "email", "password"]

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
 
