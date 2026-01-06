from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["firstname", "lastname", "email", "subject", "message"]

        widgets = {
            "firstname": forms.TextInput(attrs={"placeholder": "Your firstname"}),
            "lastname": forms.TextInput(attrs={"placeholder": "Your lastname"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject (optional)"}),
            "message": forms.Textarea(attrs={"placeholder": "Your message", "rows": 5}),
        }