from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'Enter email',
                'id': 'username',
                'data-error': "This field is required.",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'password1',
                'data-minlength': '6',
                'data-error': "Password must have a length 6 or above.",
            }
        )
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password again',
                'id': 'password2',
                'data-minlength': '6',
                'data-error': "Password must have a length 6 or above.",
    }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다')
        return username

    def clean_password(self):
        password = self.data.get('password')
        password_confirm = self.data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('비밀번호가 다릅니다.')
        if len(password) < 6:
            raise forms.ValidationError('Password must have a length 6 or above.')
        return password_confirm

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password_confirm']
            )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_num', 'address', 'homepage']

    name = forms.CharField(
        label='Full name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'id': 'fullname',
                'data-error': "This field is required.",
            }
        )
    )

    phone_num = forms.CharField(
        label='Phone number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'id': 'phone',
                'data-minlength': '10',
                'data-error': "Please enter a valid phone number.",
            }
        )
    )

    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
                'id': 'address',
                'data-error': "This field is required.",
            }
        )
    )

    homepage = forms.URLField(
        label='Homepage',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your hompage url',
                'id': 'homepage',
                'data-error': "This field is required.",
            }
        )
    )