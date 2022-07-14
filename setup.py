from setuptools import setup
from typing import List
def get_requirements_list()->List[str]:
    """
        Description This function is going to returnt the requiremnts.txt as 
        list
    """
    with open('requirements.txt') as requirement_file:
        return requirement_file.readlines()

setup(
name='Housing Predictor',
version='0.0.1',
author='Aditya',
description='This is the 1st FSDS nov batch ML Project',
packages=['housing'],
install_requires=get_requirements_list()
)

if __name__ == '__main__':
    print(get_requirements_list())

