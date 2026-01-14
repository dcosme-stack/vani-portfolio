from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def contact_view(request):
    seo = {
        "title": f"Vanishree Kulkarni – Contact",
        "description": "Get in touch with Vanishree Kulkarni.",
        "image": request.build_absolute_uri("/static/images/og/og-video.jpg"),
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            cleaned = form.cleaned_data

            send_mail(
                subject=f"New contact message: {cleaned['subject']}",
                message=cleaned['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
    )

            messages.success(request, "Thank you for your message. I’ll get back to you soon.")
            return redirect("contact:contact")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form, "seo":seo})