from tastypie.resources import ModelResource
from pinsearch.models.location import Location
from tastypie.authorization import Authorization

class LocationResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()
        list_allowed_methods = ["post","get","put","patch"]        
        detail_allowed_methods = ["get","put","patch","delete"]

