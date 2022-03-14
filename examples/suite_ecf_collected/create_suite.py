import os
from ecflow import Defs,Suite,Task,Edit
import ecflow as ecf

def create_family(family_name:str, taskname1:str, taskname2:str) -> ecf.Family:
    family = ecf.Family(family_name,
                Task(taskname1),
                Task(taskname2),
                ecf.Edit(ECF_NAME='test')
                )
    return family


if __name__=='__main__':

    print("Creating suite definition")

    ECF_HOME=os.environ.get('ECF_HOME', '.')
    ECF_INCLUDE=os.environ.get('ECF_INCLUDE', '.')
    ECF_FILES=os.environ.get('ECF_FILES', '.')

    defs = ecf.Defs(
            ecf.Suite("suiteName",
                ecf.Edit(ECF_INCLUDE=ECF_INCLUDE, 
                         ECF_HOME=ECF_HOME, 
                         ECF_FILES=ECF_FILES),
                create_family('ecf', 'task1', 'task2')
                )
            )

    print(defs)
    
    print("Checking job creation: .ecf -> .job0")
    print(defs.check_job_creation())
    
    print("Saving definition to file 'suiteName.def'")
    defs.save_as_defs("suiteName.def")
