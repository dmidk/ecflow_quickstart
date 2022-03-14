# ecFlow Quickstart
Let's get started with ECFLOW! This is a repo with an extremely condensed tutorial on how to get started with ECFLOW. It is meant as a starting point for new users, from users to users.

In terms of complexity, the examples are very simple. The examples are ordered by complexity as follows:
- [*suite_no_family*](https://github.com/dmidk/ecflow_quickstart/tree/master/examples/suite_no_family)
- [*suite_with_families*](https://github.com/dmidk/ecflow_quickstart/tree/master/examples/suite_with_families)
- [*suite_ecf_collected*](https://github.com/dmidk/ecflow_quickstart/tree/master/examples/suite_ecf_collected)

## ecFlow Terms
ecFlow operates with `suites`. A suite is a collection of `families` and `tasks`. One suite could be a configuration of a model that one wants to run. Families could then be steps in the model (like preprocessing, forecast and postprocessing), and tasks could be the actual jobs that are run.

- suite
    - family1
        - task1
        - task2
    - family2
        - task3
        - task4

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