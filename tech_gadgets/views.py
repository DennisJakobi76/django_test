from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets, manufacturers
import json
from django.utils.text import slugify
from django.urls import reverse

# Create your views here.


def start_page_view(request):
    return HttpResponse("Hey das hat doch gut funktioniert!")


def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_url = reverse('gadget_slug_url', args=[
            slugify(gadgets[gadget_id]['name'])])
        return redirect(new_url)
    return HttpResponseNotFound("Gadget not found by ID")


def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None
    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget
            break
    if not gadget_match:
        raise Http404("Gadget not found by slug")
    return JsonResponse(gadget_match, safe=False)
