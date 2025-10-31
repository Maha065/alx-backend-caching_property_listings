from django.core.cache import cache
import logging

# Optional: configure logger
logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Retrieve all Property objects from cache if available,
    otherwise fetch from DB and cache the result for 1 hour.
    """
    properties = cache.get('all_properties')
    if properties is None:
        from .models import Property
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties


def get_redis_cache_metrics():
    """
    Retrieve Redis keyspace hit/miss statistics and calculate hit ratio.
    Returns a dictionary with hits, misses, and ratio.
    """
    # Get raw Redis client from django-redis
    client = cache.client.get_client(write=True)
    
    info = client.info('stats')  # Get statistics section
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses

    hit_ratio = hits / total if total > 0 else 0.0

    metrics = {
        'keyspace_hits': hits,
        'keyspace_misses': misses,
        'hit_ratio': round(hit_ratio, 4)
    }

    logger.info(f"Redis Cache Metrics: {metrics}")
    return metrics
