from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False)
    query = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Commented By {self.name} on {self.created}"
