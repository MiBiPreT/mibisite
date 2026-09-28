"""Tests for the mibisite.my_module module."""

import pytest
from mibisite.mibisite import Mibisite


@pytest.fixture
def test_site():
    """Create test Mibisite object for use in tests."""
    return Mibisite("Test Site")


def test_site_creation():
    """Test creation of Mibisite object."""
    name = "My Site"
    mysite = Mibisite(name)
    assert mysite.name == name


# def test_load_wells(test_site):
#     """Test well addition."""
#     test_site.load_wells("/examples/data/wells.csv")
#     assert test_site.observation_wells
