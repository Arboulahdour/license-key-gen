from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from license_key_gen.serializers import LicenseKeyGenSerializer
from license_key_gen.models import License_key_gen

import random

### Open Source Algorithm To Generate Random License Keys :

class Key:

	def __init__(self, key=''):
		if key == '':
			self.key= self.generate()
		else:
			self.key = key.lower()

	def verify(self):
		score = 0
		check_digit = self.key[0]
		check_digit_count = 0
		chunks = self.key.split('-')
		for chunk in chunks:
			if len(chunk) != 4:
				return False
			for char in chunk:
				if char == check_digit:
					check_digit_count += 1
				score += ord(char)
		if score == 1772 and check_digit_count == 5:
			return True
		return False

	def generate(self):
		key = ''
		chunk = ''
		check_digit_count = 0
		alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
		while True:
			while len(key) < 25:
				char = random.choice(alphabet)
				key += char
				chunk += char
				if len(chunk) == 4:
					key += '-'
					chunk = ''
			key = key[:-1]
			if Key(key).verify():
				return key
			else:
				key = ''

	def __str__(self):
		valid = 'Invalid'
		if self.verify():
			valid = 'Valid'
		# return self.key.upper() + ':' + valid
		return self.key.upper()

### APIs Links Section :

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def apiOverview(request):

	api_urls = {
		'List':'/license-keys-list/',
		'Detail View':'/license-keys-detail/<str:pk>/',
		'Generate':'/license-keys-generate/',
		'Delete':'/license-keys-delete/<str:pk>/',
	}

	return Response(api_urls)

### License Keys APIs Section :

@api_view(['GET'])
def licenseKeyList(request):
	keys = License_key_gen.objects.all()
	serializer = LicenseKeyGenSerializer(keys, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def licenseKeyGenerate(request):
	key = Key()
	key_object = {
			"name": str(request.data['name']),
			"license_key": str(key)
	}
	serializer = LicenseKeyGenSerializer(data=key_object)
	if serializer.is_valid():
		serializer.save() 
	return Response(serializer.data)

@api_view(['GET'])
def licenseKeyDetail(request, pk):
	key = License_key_gen.objects.get(id=pk)
	serializer = LicenseKeyGenSerializer(key, many=False)
	return Response(serializer.data)

@api_view(['DELETE'])
def licenseKeyDelete(request, pk):
	key = License_key_gen.objects.get(id=pk)
	key.delete()
	return Response("key successfully deleted!")
