from django.db import models

# https://github.com/stefanfoulis/django-phonenumber-field, https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    # code = models.TextField()

    class Meta:
        ordering = ["created"]
