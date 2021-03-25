from django.db import models

# Create your models here.

class License_key_gen(models.Model):
	name = models.CharField(max_length=100)
	license_key = models.CharField(max_length=30, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.license_key