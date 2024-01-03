# shortener/models.py
from django.db import models
import hashlib
import secrets

class Link(models.Model):
    original_url = models.URLField(unique=False) 
    short_code = models.CharField(max_length=8, unique=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            
            self.short_code = self.generate_unique_short_code()
        super().save(*args, **kwargs)

    def generate_unique_short_code(self):
        
        while True:
            candidate = hashlib.sha256(secrets.token_bytes(32)).hexdigest()[:8]
            if not Link.objects.filter(short_code=candidate).exists():
                return candidate
