from setuptools import find_packages,setup # type: ignore
from typing import List
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements






setup(
name='mlproject',
version='0.0.1',
author= 'Mahim',
author_email= 'kumawatmahim@gmai1.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
)
