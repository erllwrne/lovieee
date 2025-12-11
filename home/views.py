# home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GirlfriendLoginForm
from .models import AllowedUser, Card

def login_view(request):
    if request.method == "POST":
        form = GirlfriendLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"].strip()
            anniversary = form.cleaned_data["anniversary"]
            match = AllowedUser.objects.filter(name__iexact=name, anniversary=anniversary).first()
            if match:
                request.session["girlfriend_logged_in"] = True
                request.session["girlfriend_name"] = match.name
                return redirect("home")
            else:
                # exact message requested
                context = {"form": form, "error_message": "Your not my Girlfriend 🤬🤬"}
                return render(request, "home/login.html", context)
    else:
        form = GirlfriendLoginForm()
    return render(request, "home/login.html", {"form": form})

def home_view(request):
    if not request.session.get("girlfriend_logged_in"):
        return redirect("login")
    cards = Card.objects.order_by("slot")
    return render(request, "home/home.html", {"cards": cards, "name": request.session.get("girlfriend_name")})

def card_detail(request, slot):
    if not request.session.get("girlfriend_logged_in"):
        return redirect("login")
    card = get_object_or_404(Card, slot=slot)
    return render(request, "home/card.html", {"card": card, "name": request.session.get("girlfriend_name")})

def logout_view(request):
    request.session.flush()
    return redirect("login")
