from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES=(
    (GENDER_MALE,"Male"),
    (GENDER_FEMALE,"Female"),
    (GENDER_OTHER,"Other")

    )
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_NEPALI = "nepali"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH,"English"),(LANGUAGE_NEPALI,"Nepali"))

    CURRENCY_USD ="usd"
    CURRENCY_NPR = "npr"

    CURRENCY_CHOICES = ((CURRENCY_USD,"USD"),(CURRENCY_NPR,"NPR"))

    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True,upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES,max_length=10)
    birthdate = models.DateField(blank=True,null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length =7,blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES,max_length =3,blank=True)
    superhost = models.BooleanField(default=False)





