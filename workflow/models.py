# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class TableSystemInfo(models.Model):
    system_name = models.CharField(verbose_name="系统名称", max_length=30)

    def __unicode__(self):
        return self.system_name


class TableControlFlow(models.Model):
    system_name = models.ForeignKey(to="TableSystemInfo", verbose_name="系统名称")
    TASK_TP_CHOICE = (
        ("0", "需求"),
        ("1", "临时配合")
    )
    task_tp = models.CharField(verbose_name="任务类型", choices=TASK_TP_CHOICE, max_length=2)
    req_no = models.CharField(verbose_name="需求编号", max_length=20)
    req_name = models.CharField(verbose_name="需求名称", max_length=50)
    raise_user = models.CharField(verbose_name="需求提出人", max_length=10)
    accept_user = models.CharField(verbose_name="需求受理人", max_length=10)
    accept_date = models.DateTimeField(verbose_name="需求受理日期")
    req_context = models.TextField(verbose_name="需求内容", blank=False, max_length=500)
    req_sc_date = models.DateTimeField(verbose_name="需求上线时间", blank=True)
    TASK_STATE_CHOICE = (
        ("0", "开发中"),
        ("1", "开发结束"),
        ("2", "打包中"),
        ("3", "打包结束",),
    )
    task_state = models.CharField(verbose_name="任务状态", choices=TASK_STATE_CHOICE, max_length=2)

    FLOW_STATE_CHOICE = (
        ("0", "进行中"),
        ("1", "打包结束"),
        ("3", "已投产"),
    )
    flow_state = models.CharField(verbose_name="流程状态", choices=FLOW_STATE_CHOICE, max_length=2)
    flow_end_user = models.CharField(verbose_name="流程结束人", max_length=10, blank=True)
    flow_end_date = models.DateTimeField(verbose_name="流程结束日期", blank=True)

    def __unicode__(self):
        return self.req_name


class TableWorkItem(models.Model):
    flow = models.ForeignKey(to="TableControlFlow")
    work_item_crtdate = models.DateTimeField(verbose_name="工作项创建时间", auto_now=True)
    last_user = models.CharField(verbose_name="指派人", max_length=10)
    curr_user = models.CharField(verbose_name="处理人", max_length=10)
    work_item_context = models.TextField(verbose_name="工作内容")
    plan_start_date = models.DateTimeField(verbose_name="计划开始时间")
    plan_end_date = models.DateTimeField(verbose_name="计划结束时间")
    act_start_date = models.DateTimeField(verbose_name="实际开始时间")
    act_end_date = models.DateTimeField(verbose_name="实际结束时间")

    WORK_ITEM_STATE_CHOICE = (
        ("0", "已完成"),
        ("1", "进行中"),
        ("2", "未受理"),
    )
    work_item_state = models.CharField(verbose_name="工作项状态", choices=WORK_ITEM_STATE_CHOICE, max_length=2)
    work_item_enduser = models.CharField(verbose_name="工作项结束人", max_length=10)

    def __unicode__(self):
        return self.last_user + "指派" + self.curr_user + "受理" + self.work_item_context


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64, unique=True)
    friends = models.ManyToManyField("self", blank=True, symmetrical=True, related_name="my_friends")

    def __unicode__(self):
        return self.name
