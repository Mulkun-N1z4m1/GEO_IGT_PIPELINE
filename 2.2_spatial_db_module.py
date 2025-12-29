from sqlalchemy import create_engine
import geoalchemy2 # sqlalchemy version but for geoDB

def setup_spatial_db(connection_string='postgresql://user:pass@localhost:5432/igt_db'):
    """Establishes connection to PostGIS database."""
    engine = create_engine(connection_string)
    # Enable PostGIS extension if not exists (usually run once)
    with engine.connect() as conn:
        conn.execute('CREATE EXTENSION IF NOT EXISTS postgis;')
    return engine

def gdf_to_postgis(gdf, table_name, engine, if_exists='replace'):
    """Writes a GeoDataFrame to a PostGIS table."""
    gdf.to_postgis(table_name, engine, if_exists=if_exists, index=False)

def query_spatial_db(engine, query):
    """Executes a spatial SQL query and returns a GeoDataFrame."""
    return gpd.read_postgis(query, engine)