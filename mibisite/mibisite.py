"""Documentation about the mibisite module."""
import pandas as pd
from geopandas import GeoDataFrame
from shapely import MultiPolygon
from shapely import Point


class SiteProperties(GeoDataFrame):
    """Class deriving from GeoDataFrame holding a site perimeter, and some other properties."""

    def __init__(self, perimeter: MultiPolygon = None, depth:float = None, mean_flow_velocity:float = None, ):
        """Initialize SiteProperties object."""
        self.perimeter = perimeter
        self.depth = depth
        self.mean_flow_velocity = mean_flow_velocity


class Mibisite:
    """Class that holds can contain all data and models for a Mibipret (field/experimental) site."""

    def __init__(self, name : str):
        """Initialize SiteProperties object."""
        self.name : str = name
        self.site_properties: SiteProperties = None
        self.observation_wells = GeoDataFrame(
            columns = ["name", "coordinates", "well_type"], geometry = "coordinates",
            crs="EPSG:4326",
            )
        self.pumping_wells = GeoDataFrame(
            columns = ["name", "coordinates", "well_type"], geometry = "coordinates",
            crs="EPSG:4326",
            )


    def add_well(self, name:str, coordinates:Point, well_type:str):
        """Add a well to your Mibisite object."""
        coordinates = Point(coordinates[0], coordinates[1])
        well_dict = {
            "name": name,
            "coordinates": coordinates,
            "well_type": well_type,
            }
        df_new = GeoDataFrame(well_dict, geometry = "coordinates", crs="EPSG:4326",)
        if well_type == "observation":
            self.observation_wells = pd.concat(self.observation_wells, df_new)

        elif well_type == "pumping":
            self.pumping_wells = pd.concat(self.pumping_wells, df_new)


    def show_map(self):
        """Show the map of your fieldsite with several optional layers of information."""
        pass


    def save_sikb():
        """Store the Mibisite object as a SIKB1010 standard .xml file."""
