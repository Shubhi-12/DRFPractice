from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def endpoints(request):
    data=['advocates','advocates/:username']
    return JsonResponse(data,safe=False)


def advocates_list(request):
    data=['Alex','Bob','Martin']
    return JsonResponse(data,safe=False)

def advocate_details(request,username):
    data = username
    return JsonResponse(data,safe=False)
