from operator import mod
from pyexpat import model
from django.contrib.auth.forms import UserChangeForm,UserCreateForm
from .models import User

class CustomUserCreateForm(UserCreateForm):
    class Meta(UserCreationsForm):
        model = User
        fields = ['email','username','firstname','lastname']
        error_class="error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username','firstname','lastname']
        error_class="error"