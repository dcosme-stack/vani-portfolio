from django_ratelimit.decorators import ratelimit 
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

@ratelimit(key="ip", rate="5/m", method="POST", block=False)
def contact_view(request):
    seo = {
        "title": "Vanishree Kulkarni – Contact",
        "description": "Get in touch with Vanishree Kulkarni.",
        "image": request.build_absolute_uri("/static/images/og/og-video.jpg"),
    }

    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if getattr(request, "limited", False):
            messages.error(
                request,
                "Too many messages sent. Please wait a minute and try again."
            )
        elif form.is_valid():
            form.save()

            cleaned = form.cleaned_data

            send_mail(
                subject=f"[Vani Portfolio][Contact Message]: {cleaned['subject']}",
                message=cleaned['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
            )

            messages.success(
                request,
                "Thank you for your message. I’ll get back to you soon."
            )
            return redirect("contact:contact")

    return render(
        request,
        "contact/contact.html",
        {
            "form": form,
            "seo": seo,
        },
    )