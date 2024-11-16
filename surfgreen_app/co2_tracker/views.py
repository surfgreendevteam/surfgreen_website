from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from surfgreen_app.co2_tracker.models import CO2Data
import json

@csrf_exempt
def track_co2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session_id = data.get('session_id')
        emissions = data.get('emissions')
        path = data.get('path')

        co2_data = CO2Data(session_id=session_id, emissions=emissions, path=path)
        co2_data.save()

        return JsonResponse({'status': 'success', 'message': 'Data saved successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
