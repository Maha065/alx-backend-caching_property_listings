from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all Property objects from cache if available,
    otherwise fetch from DB and cache the result for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties
