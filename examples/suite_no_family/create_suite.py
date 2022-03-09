import os
from ecflow import Defs,Suite,Task,Edit

if __name__=='__main__':

    print("Creating suite definition")

    ECF_HOME=os.environ.get('ECF_HOME', '.')

    defs = Defs(
            Suite('suiteName',
                Edit(ECF_HOME=ECF_HOME),
                Task('task1'),
                Task('task2')))
    print(defs)
    
    print("Checking job creation: .ecf -> .job0")
    print(defs.check_job_creation())
    
    print("Saving definition to file 'suiteName.def'")
    defs.save_as_defs("suiteName.def")
