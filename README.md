## Badges

(Customize these badges with your own links, and check https://shields.io/ or https://badgen.net/ to see which other badges are available.)

| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/MiBiPreT/mibisite) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/MiBiPreT/mibisite)](https://github.com/MiBiPreT/mibisite) |
| (3/5) community registry           | [![RSD](https://img.shields.io/badge/rsd-mibisite-00a3e3.svg)](https://www.research-software.nl/software/mibisite) [![workflow pypi badge](https://img.shields.io/pypi/v/mibisite.svg?colorB=blue)](https://pypi.python.org/project/mibisite/) |
| (4/5) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>)|
| (5/5) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project=MiBiPreT_mibisite&metric=alert_status)](https://sonarcloud.io/dashboard?id=MiBiPreT_mibisite) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project=MiBiPreT_mibisite&metric=coverage)](https://sonarcloud.io/dashboard?id=MiBiPreT_mibisite) || **GitHub Actions**                 | &nbsp; |
| Build                              | [![build](https://github.com/MiBiPreT/mibisite/actions/workflows/build.yml/badge.svg)](https://github.com/MiBiPreT/mibisite/actions/workflows/build.yml) |
| Citation data consistency          | [![cffconvert](https://github.com/MiBiPreT/mibisite/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/MiBiPreT/mibisite/actions/workflows/cffconvert.yml) || SonarCloud                         | [![sonarcloud](https://github.com/MiBiPreT/mibisite/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/MiBiPreT/mibisite/actions/workflows/sonarcloud.yml) |## How to use mibisite

Python package to generate a Mibipret Site object, the first step and central data structure in a Mibipret workflow

The project setup is documented in [project_setup.md](project_setup.md). Feel free to remove this document (and/or the link to this document) if you don't need it.

## Installation

To install mibisite from GitHub repository, do:

```console
git clone git@github.com:MiBiPreT/mibisite.git
cd mibisite
python -m pip install .
```

## Documentation

Include a link to your project's full documentation here.

## Contributing

If you want to contribute to the development of mibisite,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).


## Mibisite design docs

### Purpose

`mibisite` combines and standardizes the various data that are relevant to bioremediation modeling
and analysis into a single data object with functionality for visualization of the field site data
and exporting it to common formats.

### Types of data in a Mibisite object

- Perimeter (shapeobject) required

- Landmarks (shapeobject) optional

- Site parameters
    - Site max depth
    - Hydrological parameters (from mibitrans)
    - Attenuation parameters (from mibitrans)

- 2D/3D data fields (on regular, irregular grids)
    - mibitrans simulations

- Source
    - Point (location, depth, chemical)
    - Area (2D shapefile, chemical) future
    - Volume (3D) future
    - Source parameters (from mibitrans) ??

- Observation well (well_name, coordinates, metadata*)

- Sample (name, well_name, time, depth, variables)

- Injection wells (well_name, pumping_rate, mainly water, chemicals, nutrients, bacteria)

- Extraction wells

### Example use

from mibisite import Mibisite
import mibiscreen as mbs
import mibitrans as mbt

mysite = Mibisite()


mysite.add_well(well_type="observation", )
mysite.plot()

mbs.screen(mysite)


new_field = mbt.model(mysite)
mysite.addfield(new_field)