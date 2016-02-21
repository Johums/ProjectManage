# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import models


@login_required
def index(request):
    return render(request, "index.html")


@login_required()
def acc_logout(request):
    logout(request)
    render("/")


def acc_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "login.html", {
                "login_error": "错误的账号或者密码!"
            })
    else:
        return render(request, 'login.html')


@login_required
def create_task(request):
    if request.method == "GET":
        system_infos = models.TableSystemInfo.objects.all()
        staffs = models.UserInfo.objects.all()
        return render(request, "create_task.html", {"system_infos": system_infos, "staffs": staffs})
    if request.method == "POST":
        return HttpResponse("successful")


@login_required
def distribute_task(request):
    if request.method == "GET":

        system_name = request.GET.get("system_name", "").strip()
        req_name = request.GET.get("req_name", "").strip()
        last_user = request.GET.get("last_user", "").strip()

        work_items = models.TableWorkItem.objects.select_related().exclude(work_item_state__contains="0")\
            .filter(flow__req_name__contains=req_name)\
            .filter(last_user__contains=last_user)\
            .filter(flow__system_name__system_name__contains=system_name)
        return render(request, "distribute_task.html", {"work_items": work_items})


@login_required
def task_details(request, workitem_id):
    workitem = models.TableWorkItem.objects.select_related().get(id=workitem_id)
    return render(request, "task_details.html", {"work_items": workitem})
