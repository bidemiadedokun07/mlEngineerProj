from setuptools import find_packages
from setuptools import setup
from typing import List

hypen_e_dot = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ] #to replace new line "\n" with blank to avoid errors 
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name= 'mlEngineerProj',
    version='0.0.1',
    author='Bidemi',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)