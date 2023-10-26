from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Place


def show_map(request):
    places = Place.objects.all()
    serialize_places = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places.iterator():
        serialize_places["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('places', args=(place.pk,))
                }
            }
        )
    return render(request, template_name="index.html", context={"places": serialize_places})


def get_page_with_place(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=place_id)
    place_images = place.images.all()
    images = [place_image.image.url for place_image in place_images]
    serialize_place = {
        "title": place.title,
        "imgs": images,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude
        }
    }
    return JsonResponse(serialize_place, json_dumps_params={'ensure_ascii': False, 'indent': 2})
