# Define a method for displaying Earth Engine image tiles on a folium map.
def add_ee_layer(self, ee_object, vis_params, name):
    
    try:    
        # display ee.Image()
        if isinstance(ee_object, ee.image.Image):    
            map_id_dict = ee.Image(ee_object).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.ImageCollection()
        elif isinstance(ee_object, ee.imagecollection.ImageCollection):    
            ee_object_new = ee_object.mosaic()
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.Geometry()
        elif isinstance(ee_object, ee.geometry.Geometry):    
            folium.GeoJson(
            data = ee_object.getInfo(),
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
        # display ee.FeatureCollection()
        elif isinstance(ee_object, ee.featurecollection.FeatureCollection):  
            ee_object_new = ee.Image().paint(ee_object, 0, 2)
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
    
    except:
        print("Could not display {}".format(name))
    
def add_geometry(min_lon,max_lon,min_lat,max_lat):
    import ee
    geom = ee.Geometry.Polygon(
        [[[min_lon, max_lat],
          [min_lon, min_lat],
          [max_lon, min_lat],
          [max_lon, max_lat]]])
    return(geom)

def get_l8_image(date,geometry,bands):
    import ee
    l8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT')
    l8_img = l8.filterDate(date).filterBounds(geometry).select(bands).first()
    return(l8_img)

def get_s2_image(date,geometry,bands):
    import ee
    s2 = ee.ImageCollection('COPERNICUS/S2')
    s2_img = s2.filterDate(date).filterBounds(geometry).select(bands).first()
    return(s2_img)
