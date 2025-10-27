from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .dummy_data import gadgets, manufacturers
import json
from django.utils.text import slugify

# Create your views here.


def start_page_view(request):
    return HttpResponse("Hey das hat doch gut funktioniert!")


def single_gadget_view(request, gadget_id):
    return JsonResponse(slugify(gadgets[gadget_id]['name']), safe=False)


def single_gadget_slug_view(request, gadget_slug):
    gadget_match = {"result": "nothing"}
    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget
            break
    return JsonResponse(gadget_match, safe=False)
