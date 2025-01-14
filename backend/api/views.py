from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body=request.body  #byte string of JSON data
    data={}
    dictionary_params=dict(request.GET)
    print(f"this is query paramaters",dictionary_params)
    try:
        data=json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(data)