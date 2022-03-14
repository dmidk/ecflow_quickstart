# examples/suite_with_families
This is a suite with where we collect all ecFlow files (`.ecf`) in one directory for a simpler overview. Also `header.h` and `tail` are located in `ecf` to have everything related to ecFlow in one place.

The suite is called `suiteName` and have two families, `family1` and `family2`. Each family has two tasks (or children), `task1` and `task2`.

The actual jobs that are performed are defined in the `.ecf` files in the `ecf` directory. Here scripts or pure code can called and/or be defined.

The scripts that we want to run are in the directory `scr`.

## Setting up and running the suite
1. Load the right environment. First you may want to edit `env.sh` to set the correct paths to ECF_HOME and ECF_INCLUDE.
2. Create a suite definition file: 
`python create_suite.py`
The suite definition file is `suiteName.def` in the top level directory of this example.
3. Load the suite definition file into ecFlow: `ecflow_client --load suiteName.def`
4. Trigger the suite manually: `ecflow_client --begin=suiteName`