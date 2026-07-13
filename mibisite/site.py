"""Documentation about the mibisite module."""
from geopandas import GeoDataFrame
from shapely import Point, MultiPolygon


class SiteProperties(GeoDataFrame):
    """Class deriving from GeoDataFrame holding a site perimeter (MULTIPOLYGON), and some mean properties, e.g. "mean flow velocity""""
    def __init__(self, perimeter: MultiPolygon, depth:float):
        self.perimeter = perimeter
        self.depth = depth


class WellCollection(GeoDataFrame):
    """ Collection of wells of a specific type as GeoDataFrame with well locations (POINT), and variables per well as timeseries"""
    well_type: str = None

    def __init__(self, name, location: Point, depth: float):
        self.name = name
        self.location = location
        self.depth = depth


class Measurement(TimeSeries):

    measurement_type: str = None


class Site:
    """Class that holds can contain all data and models for a Mibipret (field/experimental) site.


    """

    name: str = None
    site_properties: SiteProperties = None
    obs_wells: WellCollection = None
    pumping_wells: WellCollection = None

