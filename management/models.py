from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


# Create your models here.

class Dipendente(models.Model):
    nick = models.CharField(max_length=200)
    ruolo = models.CharField(max_length=200)
    sede = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Dipendenti"

    def __str__(self):
        return self.nick
