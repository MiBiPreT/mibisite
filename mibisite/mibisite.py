"""Documentation about the mibisite module."""
from geopandas import GeoDataFrame
from shapely import Point, MultiPolygon


class SiteProperties(GeoDataFrame):
    """Class deriving from GeoDataFrame holding a site perimeter (MULTIPOLYGON), and some mean properties, e.g. "mean flow velocity""""
    def __init__(self, perimeter: MultiPolygon, depth:float):
        self.perimeter = perimeter
        self.depth = depth


class ObservationWell(GeoDataFrame):
    """ Collection of wells of a specific type as GeoDataFrame with well locations (POINT), and variables per well as timeseries"""

    def __init__(self, name, location: Point, depth: float):
        self.name = name
        self.location = location
        self.depth = depth
        self.type = "observation"

class PumpingWell(GeoDataFrame):
       """ Collection of wells of a specific type as GeoDataFrame with well locations (POINT), and variables per well as timeseries"""
        well_type: str = None

        def __init__(self, name, location: Point, depth: float):
            self.name = name
            self.location = location
            self.depth = depth
            self.type = "pumping"

class Measurement(TimeSeries):

    measurement_type: str = None


class Mibisite:
    """Class that holds can contain all data and models for a Mibipret (field/experimental) site.
    """

    def __init__(self):
        self.name: str = None
        self.site_properties: SiteProperties = None
        self.observation_wells = {}
        self.pumping_wells = {}


    def add_well(self, well):
        if well.type == "observation":
            self.observation_wells[well.name] = well
        elif well.type == "pumping":
            self.pumping_wells[well.name] = well




