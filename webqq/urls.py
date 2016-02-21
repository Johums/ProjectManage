from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.dashboard, name="chat"),
    url(r'^send_msg/$', views.send_msg, name="chat_send_msg"),
]
