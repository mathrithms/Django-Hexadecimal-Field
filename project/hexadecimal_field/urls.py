from django.urls import path

from hexadecimal_field import views

urlpatterns = [

    path("hex_json/",views.hex_json),
]
