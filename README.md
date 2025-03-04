# Modular_Programming_project
1. Creating your python environment
    1. Create new ENvironment 

    python -m venv venv 

    2. Activate your environment 
    venv/Scripts/activate

    3. Install your requirements file 

    pip install -r requiements.txt


 --------------------------

 2. Creating your setup file 
    1. In the setup.py file we will write variable names in uppercase 
    2. we will add the "-e ." in the end of the requiremenst.txt so that it build 
        2.1 Now to take care of multiple time the dependencies are not being created we will remove it in the function of get_requirement_list()
    3. Create the get_requirements_list() function-> List(str):
         3.1 it will take care of replacing the  hideden "\n" with "" , when we readfrom the file 
         3.2 it will take care of the "-e ." removing from the List comprehension  