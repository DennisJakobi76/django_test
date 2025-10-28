from hashlib import new
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets, manufacturers
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView

# Create your views here.


def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})


class RedirectToGadgetView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'gadget_slug_url'

    def get_redirect_url(self, *args, **kwargs):
        new_kwargs = {'gadget_slug': slugify(
            gadgets[kwargs.get('gadget_id', 0)]['name'])}
        return super().get_redirect_url(*args, **new_kwargs)


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_url = reverse('gadget_slug_url', args=[
            slugify(gadgets[gadget_id]['name'])])
        return redirect(new_url)
    return HttpResponseNotFound("Gadget not found by ID")


class GadgetView(View):
    def get(self, request, gadget_slug=""):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadget_slug:
                gadget_match = gadget
                break
        if not gadget_match:
            raise Http404("Gadget not found by slug")
        return JsonResponse(gadget_match, safe=False)

    def post(self, request, gadget_slug=""):
        try:
            data = json.loads(request.body)
            # Here you would typically process the data and save it
            return JsonResponse({"data_received": data}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"response": "Das hat nicht funktioniert"}, status=400)


# def single_gadget_view(request, gadget_slug=""):
#     if request.method == 'GET':
#         gadget_match = None
#         for gadget in gadgets:
#             if slugify(gadget['name']) == gadget_slug:
#                 gadget_match = gadget
#                 break
#         if not gadget_match:
#             raise Http404("Gadget not found by slug")
#         return JsonResponse(gadget_match, safe=False)
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             # Here you would typically process the data and save it
#             return JsonResponse({"data_received": data}, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({"response": "Das hat nicht funktioniert"}, status=400)
#     return JsonResponse({"status": "error", "message": "Only POST method is allowed"}, status=405)
