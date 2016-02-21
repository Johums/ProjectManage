from __future__ import unicode_literals

from workflow import models as workflow_models
from django.db import models

class QQGroup(models.Model):
    name = models.CharField(max_length=64)
    brief = models.TextField(max_length=1024, default="nothing")
    founder = models.ForeignKey(workflow_models.UserInfo)
    admin = models.ManyToManyField(workflow_models.UserInfo, related_name="group_admins")
    members = models.ManyToManyField(workflow_models.UserInfo, related_name="group_members")
    member_limit = models.IntegerField(default=200)

    def __unicode__(self):
        return self.name