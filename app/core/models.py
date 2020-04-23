
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

"""
One of the most powerful parts of Django is the automatic admin interface. Best thing is that you can customise it easily.
If logged in as a superuser, you have access to create, edit, and delete any object (models).
You can create staff user using staff flag. The “staff” flag controls whether the
user is allowed to log in to the admin interface (i.e., whether that user is considered a “staff member” in your organization).
Since this same user system can be used to control access to public (i.e., non-admin) sites, this flag differentiates
between public users and administrators.
“Normal” admin users – that is, active, non-superuser staff members – are granted admin
access through assigned permissions. Each object editable through the admin interface has
three permissions: a create permission, an edit permission and a delete permission for all the models you had created.
Django’s admin site uses a permissions system that you can use to give specific users access
only to the portions of the interface that they need. When you create a user,
that user has no permissions, and it’s up to you to give the user specific permission
"""


class UserManager(BaseUserManager):



    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        # Checking None as a Email(testing)
        if not email:
            raise ValueError('Users must have an email address')


        user = self.model(email=self.normalize_email(email), **extra_fields)  # normalized email to make smaller case
        user.set_password(password) # coming from the BaseUserManager
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and saves a new super user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
