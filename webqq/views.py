import json
from django.shortcuts import render, HttpResponse


def dashboard(request):
    return render(request, 'webqq/dashboard.html')


def send_msg(request):
    data = request.POST.get("data")
    print json.loads(data)
    return HttpResponse("ddddd")