from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from hostels.models import HostelsNY

def home(request):
	return render(request, 'hostels/home.html')

def info(request):
	return render(request, 'hostels/info.html')

@api_view(['GET'])
def get_hostels(request):
	result = HostelsNY.objects.all()
	data = serializers.serialize('json', result)
	return Response(data, status=status.HTTP_200_OK, content_type='application/json')

@api_view(['GET'])
def hostels_filter(request):
	request_data = request.QUERY_PARAMS
	filtered_fields = request_data['fields']

	kwargs = {}

	if "name" in filtered_fields:
		kwargs['name'] = request_data['name']
	if "type" in filtered_fields:
		kwargs['type'] = request_data['type']
	if "price" in filtered_fields:		
		kwargs['price'] = request_data['price']
	if "wifi" in filtered_fields:
		kwargs['wifi'] = request_data['wifi']
	if "breakfast" in filtered_fields:
		kwargs['breakfast'] = request_data['breakfast']

	try:
		result = HostelsNY.objects.filter(**kwargs)
		data = serializers.serialize('json', result)
		return Response(data, status=status.HTTP_200_OK, content_type='application/json')
		
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)

