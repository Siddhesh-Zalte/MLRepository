#responsible for making ML project as a package
from setuptools import find_packages,setup
from typing import List
hypenE="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if hypenE in requirements:
            requirements.remove(hypenE)

    return requirements

setup(
    name="MLProject",
    version='0.0.1',
    author="Siddhesh",
    author_email='zaltesiddheshlsg@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)