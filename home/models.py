# home/models.py
from django.db import models

class AllowedUser(models.Model):
    name = models.CharField(max_length=200)
    anniversary = models.DateField(help_text="YYYY-MM-DD")

    def __str__(self):
        return f"{self.name} - {self.anniversary.isoformat()}"

class Card(models.Model):
    CARD_CHOICES = (
        (1, "Card 1"),
        (2, "Card 2"),
    )
    slot = models.IntegerField(choices=CARD_CHOICES, unique=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="cards/")
    letter = models.TextField(help_text="Love letter or quote for this card")

    def __str__(self):
        return f"Card {self.slot}: {self.title or '(no title)'}"
