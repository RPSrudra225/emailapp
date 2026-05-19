import requests
from django.shortcuts import render
from django.http import HttpResponse


RESEND_API_KEY = "YOUR_RESEND_API_KEY"


def home(request):
    return render(request, "home.html")


def send_email(request):
    url = "https://api.resend.com/emails"

    payload = {
        "from": "onboarding@resend.dev",
        "to": ["your_email@example.com"],
        "subject": "Hello from Django",
        "html": "<h1>Hello World Email from Django + Render</h1>"
    }

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return HttpResponse("Email Sent Successfully!")
    else:
        return HttpResponse(
            f"Failed: {response.text}"
        )