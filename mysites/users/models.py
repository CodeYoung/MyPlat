# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .managers import UserInheritanceManager, UserManager


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    email = models.EmailField(
        _('email address'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):

    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """
    Code=models.CharField(max_length=20,default='0011')
    Name=models.CharField(max_length=20,default='firstlogin')
    IDCard=models.CharField(max_length=20,default='511028199006201814')
    YBCard=models.CharField(max_length=20,default='yb110')
    Phone=models.CharField(max_length=11,null=True)
    #Email=models.CharField(max_length=100,null=True)
    WeChat=models.CharField(max_length=100,null=True)
    Age=models.IntegerField(default=20)
    Sex=models.CharField(max_length=10,default='男')
    FingerPrint=models.CharField(max_length=1000,null=True)
    PassWord=models.CharField(max_length=18,default='123')
    Cipher=models.CharField(max_length=6,default='123456')
    CreateTime=models.DateTimeField(default=timezone.now)
    LastLogTime=models.DateTimeField(default=timezone.now)
    Remark=models.CharField(max_length=1000,null=True)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
