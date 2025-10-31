from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    # Serialize for JSON response
    properties_data = [
        {
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'location': p.location,
            'created_at': p.created_at.isoformat()
        }
        for p in properties
    ]
    return JsonResponse(properties_data, safe=False)
