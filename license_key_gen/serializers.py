from rest_framework import serializers
from .models import License_key_gen

class LicenseKeyGenSerializer(serializers.ModelSerializer):
	class Meta:
		model = License_key_gen
		fields = ('id',
				  'name', 
			      'license_key', 
			      'created_at')