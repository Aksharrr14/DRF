from django.http import JsonResponse
import json

from rest_framework.response import Response

def api_home(request, *args, **kwargs):
    return JsonResponse({"hi":"akshar"})