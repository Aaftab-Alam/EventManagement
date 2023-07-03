from djongo import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, Group, Permission

# class CustomUser(AbstractUser):
#     # pass
#     # Your custom fields and methods here
#
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_('The groups this user belongs to.'),
#         related_name='customuser_set'  # Add a custom related name
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name='customuser_set'  # Add a custom related name
#     )



class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.username

    class Meta:
        db_table = 'Users'
