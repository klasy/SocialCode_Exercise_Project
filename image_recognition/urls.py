# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
#from image_recognition import views


#urlpatterns = patterns('SocialCode_Exercise_Project.image_recognition.views',
#    url(r'^upload/$', 'upload', name='upload'),
#)

urlpatterns = patterns('image_recognition.views',
        url(r'^$', 'upload_handler', name='upload'),
)
