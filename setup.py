from setuptools import setup, find_packages
from typing import List

requirement_lst:List[str] = []
def get_requirements(file_path: str) -> List[str]:
    try:
        with open('requirements.txt','r') as file:
            lines =file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print('File not found')

    return requirement_lst

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Ravi',
    author_email = 'ravi',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)