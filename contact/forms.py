from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        honeypot = forms.CharField(
            required=False,
            widget=forms.HiddenInput
        )
        model = ContactMessage
        fields = ["firstname", "lastname", "email", "subject", "message"]

        widgets = {
            "firstname": forms.TextInput(
                attrs={
                    "aria-describedby": "error-firstname",
                    "maxlength": 100,
                }
            ),
            "lastname": forms.TextInput(
                attrs={
                    "aria-describedby": "error-lasttname",
                    "maxlength": 100,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "aria-describedby": "error-firstname",
                    "maxlength": 254,
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "aria-describedby": "error-subject",
                    "maxlength": 150,
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Your message",
                    "rows": 5,
                    "aria-describedby": "error-message",
                    "maxlength": 2000,
                }
            ),
        }

    def clean_honeypot(self):
        if self.cleaned_data.get("honeypot"):
            raise forms.ValidationError("Bot detected.")
        return ""