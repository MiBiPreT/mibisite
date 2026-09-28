"""Documentation about the mibisite module."""
import contextily as cx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from geopandas import GeoDataFrame
from shapely import Point


class Mibisite:
    """Class that holds can contain all data and models for a Mibipret (field/experimental) site."""

    def __init__(self, name : str, perimeter_shapefile:str = None, landmarks_shapefile:str = None):
        """Initialize SiteProperties object."""
        self.name : str = name
        if perimeter_shapefile:
            self.perimeter = gpd.read_file(perimeter_shapefile).set_crs(crs="EPSG:4326")
        if landmarks_shapefile:
            self.landmarks = gpd.read_file(landmarks_shapefile).set_crs(crs="EPSG:4326")

        self.wells = None
        self.observation_wells = GeoDataFrame(
            columns = ["name", "coordinates", "well_type"], geometry = "coordinates",
            crs="EPSG:4326",
            )
        self.pumping_wells = GeoDataFrame(
            columns = ["name", "coordinates", "well_type"], geometry = "coordinates",
            crs="EPSG:4326",
            )


    def load_wells(self, wells_filename):
        """Load wells data from a csv file into the Mibisite object."""
        wells_df = gpd.read_file(wells_filename)
        self.observation_wells = GeoDataFrame(
            wells_df,
            geometry=gpd.points_from_xy(wells_df.latitude, wells_df.longitude),
            crs="EPSG:4326"
            ).drop(["latitude", "longitude"], axis=1)


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
        fig, ax = plt.subplots(figsize=(15,12))
        ax.set_title(self.name + " fieldsite", fontsize=20)
        self.perimeter.boundary.plot(ax=ax, color="green")
        self.landmarks.boundary.plot(ax=ax, color="gray")
        self.observation_wells.plot(ax=ax, column="subtype")
        cx.add_basemap(ax, alpha=0.5, crs="EPSG:4326")

