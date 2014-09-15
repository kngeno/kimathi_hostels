from django.contrib.gis import admin as geoadmin
from hostels.models import HostelsNY
#from geoportal import admin

class HostelsNYAdmin(geoadmin.OSMGeoAdmin):

    list_display = ('place','name', 'type', 'price', 'wifi', 'breakfast',)
    search_fields = ['name', 'place',]
    search_fields = ('price',)
    default_lon =  4113018.76068 #36.9654#
    default_lat =  -46755.87145  #-0.4030
    default_zoom = 14
    map_info = True
    map_width = 800
    map_height = 500

#Geoportail activation
'''
class HostelsNYAdmin(admin.GeoPortalAdmin):
    list_display = ('place','name', 'type', 'price', 'wifi', 'breakfast',)
    search_fields = ['name', 'place',]    
    map_info = True
    default_lon =  -0.4030
    default_lat =  36.9654
    default_zoom = 12
    map_width = 600
    map_height = 300
    point_zoom = 14
    layers = (
        ('maps', 1),
        ('photos', 0.3),
    )
    layerswitcher = True
'''
geoadmin.site.register(HostelsNY, HostelsNYAdmin)    
#admin.site.register(HostelsNY, HostelsNYAdmin)
