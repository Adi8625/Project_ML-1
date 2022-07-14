from setuptools import find_packages, setup
from typing import List
def get_requirements_list()->List[str]:
    """
        Description This function is going to returnt the requiremnts.txt as 
        list
    """
    with open('requirements.txt') as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
name='Housing Predictor',
version='0.0.3',
author='Aditya',
description='This is the 1st FSDS nov batch ML Project',
packages=find_packages(),
install_requires=get_requirements_list()
)


