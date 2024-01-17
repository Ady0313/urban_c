# tryon/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .config import update_config
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def update_config_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            look_uri = data.get('look_uri')
            avatar_uri = data.get('avatar_uri')

            update_config(look_uri, avatar_uri)

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# Add the following view for try-on-api
@csrf_exempt
def try_on_api(request):
    # Your logic for the try-on API
    return JsonResponse({'status': 'success'})
