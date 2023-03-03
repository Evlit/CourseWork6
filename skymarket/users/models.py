# from datetime import timezone

from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
from django.core.validators import FileExtensionValidator
from django.db import models
# from coursework_6_skymarket.skymarket.users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles(models.TextChoices):
    USER = "user", _("User")
    ADMIN = "admin", _("Admin")


class User(AbstractUser):
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'image']
    USERNAME_FIELD = 'email'

    username = None
    email = models.EmailField(verbose_name='email address', unique=True)
    last_login = models.DateTimeField(null=True, blank=True, auto_now=True)
    phone = PhoneNumberField(_('phone number'), null=False, blank=False)
    role = models.CharField(max_length=5, default=UserRoles.USER, choices=UserRoles.choices)
    image = models.ImageField(upload_to='images/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["id"]
