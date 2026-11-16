# noqa: D103

"""Tests for the mibisite.my_module module."""

import pytest
from mibisite.mibisite import Mibisite
from geopandas import GeoDataFrame


@pytest.fixture
def test_site():
    """Create test Mibisite object for use in tests."""
    return Mibisite("Test Site")

@pytest.fixture
def test_site_with_perimeter():
    perimeter_file = "./tests/data/perimeter/Perimeter.shp"
    landmarks_file = "./tests/data/landmarks/Landmarks.shp"
    return Mibisite("Test Site",perimeter_file, landmarks_file)


def test_site_creation(test_site):
    """Test creation of Mibisite object."""
    name = "My Site"
    test_site.name = name
    assert test_site.name == name

def test_perimeter_loading(test_site_with_perimeter):
    assert isinstance(test_site_with_perimeter.perimeter, GeoDataFrame)
    assert isinstance(test_site_with_perimeter.landmarks, GeoDataFrame)


def test_show_map_without_perimeter(test_site):
    """Test map plotting without perimeter raises an attribution error."""
    with pytest.raises(AttributeError):
        test_site.show_map()

def test_load_wells(test_site):
    test_site.load_wells("./tests/data/wells.csv")

@pytest.mark.parametrize(
        "type, expected_obs_shape, expected_pump_shape",
        [
            pytest.param("observation", (3,3),(0,3)),
            pytest.param("pumping", (0,3), (3,3)),
        ]
        )
def test_add_well(test_site, type, expected_obs_shape, expected_pump_shape):
    for name in ["well1", "well2", "well3"]:
        coordinates = (52.35571439098452, 4.955805663793695)
        test_site.add_well(name, coordinates, type)

    assert test_site.observation_wells.shape == expected_obs_shape
    assert test_site.pumping_wells.shape == expected_pump_shape


