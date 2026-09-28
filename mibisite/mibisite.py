"""Documentation about the mibisite module."""
from geopandas import GeoDataFrame
from shapely import MultiPolygon
from shapely import Point
import pandas as pd


class SiteProperties(GeoDataFrame):
    """Class deriving from GeoDataFrame holding a site perimeter (MULTIPOLYGON), and some mean properties, e.g. "mean flow velocity"""
    def __init__(self, perimeter: MultiPolygon, depth:float):
        self.perimeter = perimeter
        self.depth = depth


class Mibisite:
    """Class that holds can contain all data and models for a Mibipret (field/experimental) site."""

    def __init__(self, name : str):
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


    def add_well(self, name, coordinates, well_type):
        coordinates = Point(coordinates[0], coordinates[1])
        well_dict = {
            "name": name,
            "coordinates": coordinates,
            "well_type": well_type
            }
        df_new = GeoDataFrame(well_dict, geometry = "coordinates", crs="EPSG:4326",)
        if well_type == "observation":
            self.observation_wells = pd.concat(self.observation_wells, df_new)

        elif well_type == "pumping":
            self.pumping_wells = pd.concat(self.pumping_wells, df_new)


    def plot(self):
        print("Look I'm plotting!")


