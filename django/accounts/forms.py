from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email',
                             error_messages={'exists': 'Oops - email already taken'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class QueuedPasswordResetForm(PasswordResetForm):
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        print(f">>>>>>>>>>>>> ------- >>>>>> send_mail(from: {from_email}, to: {to_email}")
        super().send_mail(subject_template_name, email_template_name,
                          context, from_email, to_email, html_email_template_name)
