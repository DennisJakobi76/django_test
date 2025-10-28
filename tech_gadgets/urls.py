
from turtle import st
from django.urls import path
from .views import RedirectToGadgetView, single_gadget_int_view, GadgetView, start_page_view


urlpatterns = [
    path('start/', start_page_view),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>',
         GadgetView.as_view(), name='gadget_slug_url'),

]
