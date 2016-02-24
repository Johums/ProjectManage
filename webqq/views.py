import json
import datetime
from django.shortcuts import render, HttpResponse
import models

import utils

global_msg_dic = dict()


def dashboard(request):
    return render(request, 'webqq/dashboard.html')


def send_msg(request):
    data = request.POST.get("data")
    data = json.loads(data)

    to_id = data.get("to_id")
    user_obj = models.workflow_models.UserInfo.objects.get(id=to_id)
    contact_type = data.get("contact_type")

    data["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not global_msg_dic.has_key(request.user.id):
        global_msg_dic[to_id] = utils.Chat()
    global_msg_dic[to_id].msg_queue.put(data)

    print "\033[32;1mI Push msg [%s] into user [%s] queue" % (data["msg"], user_obj.name)
    print "global_msg_dic = ", global_msg_dic
    return HttpResponse("ddddd")


def get_msg(request):
    uid = request.GET.get("uid")
    print uid
    if uid:
        res = list()
        if global_msg_dic.has_key(uid):
            res = global_msg_dic[uid].get_msg()
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided! "))
