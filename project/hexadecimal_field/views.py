from django.shortcuts import render
from django.http import JsonResponse
from hexadecimal_field.models import hexadecimal

def hex_json(request):
    results = {
        "hexadecimal":[],
    }

    for hex in hexadecimal.objects.all():
        line = [str(hex), []]
        for item in hex.item_set.all():
            line[1].append(str(item))

        results["hexadecimal"].append(line)

    return JsonResponse(results)
