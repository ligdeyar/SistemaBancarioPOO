from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SistemaBancario.models import *
from SistemaBancario.serializers import *

# Create your views here.
