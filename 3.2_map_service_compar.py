import requests
import folium

def compare_with_google_maps(api_key, location_name, your_data_geometry):
    """Fetches polygon from Google Maps Geocoding API for comparison."""
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location_name}&key={api_key}'
    response = requests.get(url).json()
    # Parse response to get bounds or geometry
    # ... (geometry extraction logic)
    # google_geom = ...
    # Calculate similarity metric (e.g., area ratio, intersection area)
    intersection_area = your_data_geometry.intersection(google_geom).area
    union_area = your_data_geometry.union(google_geom).area
    iou_score = intersection_area / union_area if union_area > 0 else 0
    return iou_score, google_geom

def visualize_comparison(your_gdf, service_geom, service_name):
    """Creates an interactive map to visually compare geometries."""
    m = your_gdf.explore(
        name='Authoritative Data (IGT)',
        color='blue',
        style_kwds={'fillOpacity': 0.5}
    )
    folium.GeoJson(service_geom, name=service_name).add_to(m)
    folium.LayerControl().add_to(m)
    return m