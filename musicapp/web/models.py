from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from musicapp.web.validators import contains_only_letters_numbers_and_underscore


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            #TODO: Ask
            # We make migration for the class before making migration for the Profile
            contains_only_letters_numbers_and_underscore,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC ='R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC ='Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    MUSICS = (
        ('POP MUSIC', 'POP MUSIC'),
        ('Jazz Music', 'JAZZ MUSIC'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'ROCK MUSIC'),
        ('Country Music', 'COUNTRY MUSIC'),
        ('Dance Music', 'DANCE MUSIC'),
        ('Hip Hop Music', 'HIP HOP MUSIC'),
        ('Other', 'OTHER'),
    )
    album_name = models.CharField(
        max_length=30,
        verbose_name='Album Name',
        null=False,
        blank=False,
        unique=True,
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=MUSICS,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        ),
    )

    class Meta:
        ordering = ('pk',)
