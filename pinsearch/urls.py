from django.conf.urls import patterns, include, url
from django.conf.urls import *
from tastypie.api import Api
from pinsearch.views import location
from pinsearch.api.location import LocationResource


v1_api = Api(api_name='v1')
v1_api.register(LocationResource())


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', index.index),
	# (r'^admin/', include(admin.site.urls)),
	(r'', include(v1_api.urls)),
	url(r'^v0/location/$',location.locationSearch),
)

