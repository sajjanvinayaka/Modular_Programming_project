# from distutils.core import setup
from setuptools import setup, find_packages
from typing import List 

# The culture in setup file the variables are in capitalised 


PROJECT_NAME = "Machime Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is our machine learning project in modular coding"
AUTHOR_NAME = "Sajjanshetty Vinayaka"
AUTHOR_EMAIL = "dummy`successanalytics.ai"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

#Requirements.txt file open 
#read
#\n is hidden when we use the readlines, we will replace with ""
def get_requiremets_list()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME ) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
            
        return requirement_list
        
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires = get_requiremets_list() 
     )

"""
find_packages : will go into your src folder starts finding the 
__init__.y files to create the package 
"""