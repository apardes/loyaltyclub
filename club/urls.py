from django.conf.urls import patterns, include, url
from django.contrib import admin
from club import views

urlpatterns = patterns('',
	url(r'^', views.index, name = 'index'),
	url(r'^issue/$', views.issueCredit, name = 'issueCredit'),
	url(r'^charge/$', views.chargeCredit, name = 'chargeCredit'),
)
