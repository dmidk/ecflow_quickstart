# ECFLOW Quickstart
Let's get started with ECFLOW! This is a repo with an extremely condensed tutorial on how to get started with ECFLOW. It is meant as a starting point for new users, from users to users.

## Prerequisites
- ecflow
- python

### Install ecflow using conda
In these examples an installation from a conda environment was used. The `yaml` file was defined as follows:
```yaml
name: ec
channels:
    - conda-forge
dependencies:
    - python
    - pip
    - ecflow
```
And the environment was created as follows:
```bash
conda env create -f ec.yaml
```