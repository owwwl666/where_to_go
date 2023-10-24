from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Place, PlaceImage


def show_map(request):
    places = Place.objects.all()
    places_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places.iterator():
        places_json["features"].append(
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
    return render(request, template_name="index.html", context={"places": places_json})


def get_page_with_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = PlaceImage.objects.filter(place=place)
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
