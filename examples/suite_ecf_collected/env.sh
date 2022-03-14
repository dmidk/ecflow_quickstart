#!/bin/bash

#The first thing ecFlow does is to change the current working directory (or CWD) into ECF_HOME, 
#so all the other files listed there are read from that directory (unless full path names are used).
export ECF_HOME=$HOME/git/ecflow_quickstart/examples/suite_ecf_collected/
export ECF_INCLUDE=$HOME/git/ecflow_quickstart/examples/suite_ecf_collected/suiteName/ecf/
#export ECF_FILES=$HOME/git/ecflow_quickstart/examples/suite_ecf_collected/suiteName/

export ECF_FETCH=$HOME/git/ecflow_quickstart/examples/suite_ecf_collected/ecf/
#export ECF_SCRIPT_CMD=

export ECF_CHECKINTERVAL=20