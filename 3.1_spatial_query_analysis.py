def analyze_polygonal_overlap(gdf_admin, gdf_land_use):
    """Performs spatial join to find land use within administrative boundaries."""
    # Ensure same CRS
    gdf_land_use = gdf_land_use.to_crs(gdf_admin.crs)
    # Spatial join: what land use is within each admin region?
    joined = gpd.sjoin(gdf_land_use, gdf_admin, how='inner', predicate='intersects')
    # Calculate area of each land use type per province
    joined['area_ha'] = joined.geometry.area / 10000
    summary = joined.groupby(['province_name', 'landuse_type'])['area_ha'].sum().reset_index()
    return summary

def perform_spatial_query(gdf, target_geometry, operation='intersects'):
    """Queries a GeoDataFrame based on a spatial relationship."""
    if operation == 'intersects':
        mask = gdf.geometry.intersects(target_geometry)
    elif operation == 'within':
        mask = gdf.geometry.within(target_geometry)
    elif operation == 'contains':
        mask = gdf.geometry.contains(target_geometry)
    return gdf[mask]