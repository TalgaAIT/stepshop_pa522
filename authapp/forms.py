from django.contrib.auth.forms import AuthenticationForm

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        Fields = ('username', 'password')