from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import UserManager
from django.contrib.auth.models import UserManager
from django.db import models


class PermissionMixin(object):
    pass


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        # user = super().create_user(email, password, password, **extrafields)
        return user

    def create_superuser(self, email, password=None, **extrafields):
        user = self.create_user(email=email, password=password, sword=None, **extrafields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class USER(AbstractBaseUser, PermissionMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.id}, {self.email}"

    def has_perm(self, perm, obj = None):
        if self.is_active and self.is_staff:
            return True
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        return self.is_staff

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'
