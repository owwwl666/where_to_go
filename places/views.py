from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
                    "detailsUrl": ""
                }
            }
        )
    return render(request, template_name="index.html", context={"places": places_json})


def get_page_with_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = PlaceImage.objects.filter(place=place)
    images = [place_image.image.url for place_image in place_images]
    place_data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude
        }
    }
    return JsonResponse(place_data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
