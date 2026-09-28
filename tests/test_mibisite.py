"""Tests for the mibisite.my_module module."""

import pytest
from mibisite.mibisite import Mibisite


@pytest.fixture
def test_site():
    return Mibisite("Test Site")

def test_site_creation():
    name = "My Site"
    mysite = Mibisite(name)
    assert mysite.name == name

def test_add_well(test_site):
    test_site.add_well("p51vf", [4.9041, 52.3676], well_type="observation")
    assert test_site.observation_wells