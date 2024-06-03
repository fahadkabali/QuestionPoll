from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Applying Bootstrap 'form-control' class to all visible fields
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class SignupForm(UserCreationForm, FormSettings):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            instance = kwargs.get('instance').__dict__
            self.fields['password1'].required = False
            self.fields['password2'].required = False
            for field in SignupForm.Meta.fields:
                self.fields[field].initial = instance.get(field)
            if self.instance.pk is not None:
                self.fields['password1'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
                self.fields['password2'].widget.attrs['placeholder'] = "Fill this only if you wish to update password"
        else:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True

    def clean_email(self, *args, **kwargs):
        formEmail = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if User.objects.filter(email=formEmail).exists():
                raise forms.ValidationError(
                    "The given email is already registered")
        else:  # Update
            dbEmail = self.Meta.model.objects.get(
                id=self.instance.pk).email.lower()
            if dbEmail != formEmail:  # There have been changes
                if User.objects.filter(email=formEmail).exists():
                    raise forms.ValidationError(
                        "The given email is already registered")
        return formEmail

    def clean_password1(self):
        password = self.cleaned_data.get("password1", None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password
        return make_password(password)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
