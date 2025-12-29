import geopandas as gpd # spatial data and geometric operations (polygons)
import os

def load_indonesian_data(data_path, layer_name=None):
    """Loads Indonesian spatial data from various formats."""
    if data_path.endswith('.gpkg') and layer_name:
        gdf = gpd.read_file(data_path, layer=layer_name)
    else:
        gdf = gpd.read_file(data_path)
    # Ensure consistent CRS for Indonesia
    if gdf.crs is None:
        gdf.set_crs(epsg=4326, inplace=True) # WGS84
    else:
        gdf.to_crs(epsg=4326, inplace=True)
    return gdf

# Example: Load provincial boundaries
provinsi = load_indonesian_data('KPKNLDJKN_PT_1K/KPKNLDJKN_PT_1K.shp')