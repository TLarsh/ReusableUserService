from django contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegistrationServices:
    def __init__(self, *args, *kwargs):
        self.args = args
        self.kwargs = kwargs
        self.cleaned_data = {}

    def _normalize_fields(self):
        first_name = self.kwargs.get('first_name', '')
        email = self.kwargs.get('email','')
        password  = self.kwargs.get('password', '')

        first_name = map(Lambda x: x.lower().title())