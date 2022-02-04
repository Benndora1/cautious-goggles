from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):


    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Provide a valid email address"))

    # creating a user
    def create_user(self,username,firstname,lastname,email,password,
    **extra_fields):
        if not username:
             raise ValueError(_ ("Username must not be empty"))
            
        if not firstname:
            raise ValueError(_("User must submit first name"))
        
        if not lastname:
            raise ValueError(_("User must submit last name"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))
        
        user = self.model(
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=email,
            **extra_fields
        )


        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user



        # creating a superuser
    def create_superuser(self, username,firstname,lastname,email,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        
        if extra_fields.get('is_superuser') is not True:
           raise ValueError(_("Superuser must have is_superuser=True"))

        if not password:
            raise ValueError(_("Password must not be empty"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))
          
        user = self.create_user(username, firstname,lastname,email,password,**extra_fields)
        user.save(using=self._db)
        return user
