from django.db import models


class Developer(models.Model):
    github_username = models.CharField(max_length=200)
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    avatar_url = models.CharField(max_length=255, null=True)
    techs = models.TextField(null=True)
    latitude = models.DecimalField(null=True, decimal_places=6, max_digits=10)
    longitude = models.DecimalField(null=True, decimal_places=6, max_digits=10)

    def __str__(self):
        if self.name:
            return self.name
        return self.github_username
