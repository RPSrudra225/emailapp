import os
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse

RESEND_API_KEY = os.getenv("RESEND_API_KEY")


def home(request):
    return render(request, "home.html")


def send_email(request):

    if request.method == "POST":

        receiver_email = request.POST.get("email")

        url = "https://api.resend.com/emails"

        payload = {
            "from": "onboarding@resend.dev",
            "to": [receiver_email],
            "subject": "Hello from StarkExp",
            "html": """
                <h1>Hello World</h1>
                <p>Email sent successfully from Django + Render</p>
            """,
            "reply_to": "starkexp2001@gmail.com"
        }

        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return HttpResponse(response.text)

    return redirect('/')