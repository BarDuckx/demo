from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from .models import User, Application

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        validators=[
            RegexValidator(r'^[a-zA-Z0-9]+$', 'Только латиница и цифры.'),
            MinLengthValidator(6, 'Минимум 6 символов.')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8, 'Минимум 8 символов.')]
    )
    fio = forms.CharField(
        validators=[RegexValidator(r'^[А-Яа-яЁё\s]+$', 'Только кириллица и пробелы.')]
    )
    phone = forms.CharField(
        validators=[RegexValidator(r'^8\(\d{3}\) \d{3}-\d{2}-\d{2}$', 'Формат: 8(XXX) XXX-XX-XX')]
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'fio', 'phone', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ApplicationForm(forms.ModelForm):
    start_date = forms.CharField(
        validators=[RegexValidator(r'^\d{2}\.\d{2}\.\d{4}$', 'Формат: ДД.ММ.ГГГГ')]
    )

    class Meta:
        model = Application
        fields = ['course_name', 'start_date', 'payment_method']