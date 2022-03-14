import os
import ecflow as ecf

ECF_HOME=os.environ.get('ECF_HOME', '.')
ECF_INCLUDE=os.environ.get('ECF_INCLUDE', '.')
ECF_FILES=os.environ.get('ECF_FILES', '.')


def create_suite(name, families:list, ecfdir:str) -> ecf.Suite:
    suite = ecf.Suite(name)
    suite.add_variable("ECF_INCLUDE", ECF_INCLUDE)
    suite.add_variable("ECF_FILES", ECF_FILES)
    suite.add_variable("ECF_HOME", ECF_HOME)


    for family in families:
        fam = suite.add_family(family)
        fam.add_variable("FAMILY", 'ecf')
        for t in ["task1", "task2"] :
            fam.add_task(t)

    return suite


if __name__=='__main__':

    print("Creating suite definition")

    suite = create_suite('suiteName', ['familyName1', 'familyName2'], 'ecf')
    defs = ecf.Defs(suite)

    # If you want to do it more custom made, you can use the following as template:
    # defs = Defs(
    #         Suite("suiteName",
    #             Edit(ECF_INCLUDE=ECF_INCLUDE,
    #                 ECF_HOME=ECF_HOME,
    #                 ECF_FILES=ECF_FILES),
    #             Family("Family1",
    #                 Edit(FAMILY='ecf'),
    #                 Task("task1"),
    #                 Task("task2")
    #         )))

    print(defs)
    
    print("Checking job creation: .ecf -> .job0")
    print(defs.check_job_creation())
    
    print("Saving definition to file 'suiteName.def'")
    defs.save_as_defs("suiteName.def")
