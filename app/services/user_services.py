from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegistrationServices:
    '''
    Resusable registration handler that suppports custom user models,
    mapping, cleaning, and validation.
    '''

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.cleaned_data = {}
        
    def _normalize_fields(self):
        first_name = self.kwargs.get('first_name', '')
        last_name = self.kwargs.get('last_name', '')
        email = self.kwargs.get('email', '')
        password = self.kwargs.get('password', '')

        first_name, last_name = map(lambda x: x.lower().title())

        self.cleaned_data.update({
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'username':email,
            'password':password
        })

        extra_fields = {k: v for k, v in self.kwargs.items() if k not in self.cleaned_data}
        self.cleaned_data.update(extra_fields)

    def _validate_data(self):
        '''
        validating required fields and unique constraints
        '''
        required_fields = ['email', 'password', 'first_name', 'last_name']
        missing = [f for f in required_fields if not self.cleaned_data.get(f)]

        if missing:
            raise ValidationError(f"missing required fields: {','.join(missing)}")
        
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('User with this email already exists')
        
        def register(self):
            self._normalise_fields()
            self._validate_data()

            password = self.cleaned_data.pop('password')
            user = User(**self.cleaned_data)
            user.set_password(password)
            user.save()

            return user