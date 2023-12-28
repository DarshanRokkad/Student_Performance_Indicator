# This file used to make project as a package

from setuptools import find_packages, setup
from typing import List


HYPER_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    This function take the requirements.txt as input and return the package present in that file. 
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements] # all the line will have new line character at the end of package name
    if HYPER_E_DOT in requirements: # '-e .' is used to trigger setup.py which is not a package
        requirements.remove(HYPER_E_DOT)
    return requirements


setup(
    name='marks_prediction_project_package',
    version='0.0.1',
    author='DarshanRM',
    author_email='darshanrokkad2003@gmail.com',
    packages=find_packages(), # this will find all the '__init__.py' file from all the folders
    install_requires=get_requirements('requirements.txt')
)