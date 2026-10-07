from django.conf import settings
import uuid
from django.db import models


class Category(models.Model):
    """e.g. Formal Wear, Home Decor, Hairstyles — used for browsing and filtering."""
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Pin(models.Model):
    """A single piece of visual inspiration — the core unit of the site."""

    SOURCE_CHOICES = [
        ("user", "User uploaded"),
        ("curated", "Curated by admin"),
        ("ai", "AI generated"),
    ]

    title = models.CharField(max_length=150)
    image_url = models.URLField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="pins"
    )
    tags = models.CharField(
        max_length=255, blank=True,
        help_text="Comma-separated tags, e.g. 'emerald,slip dress,formal'",
    )
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default="user")
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_pins",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Board(models.Model):
    """A user-created collection of saved pins, e.g. 'Wedding Guest Looks'."""

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="boards"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("name", "owner")  # a user can't have two boards with the same name

    def __str__(self):
        return f"{self.name} ({self.owner})"


class SavedPin(models.Model):
    """Records a user saving a pin, optionally into a specific board."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="saved_pins"
    )
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE, related_name="saves")
    board = models.ForeignKey(
        Board, on_delete=models.SET_NULL, null=True, blank=True, related_name="saved_pins"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "pin", "board")

    def __str__(self):
        return f"{self.user} saved {self.pin}"


class SearchLog(models.Model):
    """Every search a user makes — feeds the future recommendation engine."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    query = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, related_name='pins', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    description = models.TextField(blank=True, null=True)
    recipe_json = models.JSONField(blank=True, null=True)  # Stores ingredients, steps, prep time
    is_saved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title