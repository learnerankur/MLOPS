from setuptools import find_packages,setup

from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requiremets
    '''
    requirements=[]
    HYPEN_E_DOT='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # reading each ;ine of requirements.txt file, but \n will also come, 
        # Removing \n 
        requirements=[req.replace("\n","") for req in requirements]

        # removing -e . from requirements.txt to run parallely
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements



setup(
    name='ML_end_to_end',
    version='0.0.1',
    author='Ankur Chaudhary',
    author_email='abc@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
