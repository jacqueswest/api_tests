# Setup Guide

## Install Python 3:
Select the latest version from:
    
    
    https://www.python.org/downloads/release/python-370
    
For Windows select _Windows x86 executable installer_

For MAC OS, click on the _download button_
    
**NB:** For Windows ensure you tick **_Add Python 3.7 to PATH_** during installation


## Upgrade PIP(_Python package manager_)
From _cmd_ or _bash prompt_, execute:

    python -m pip install --upgrade pip
    

## Install GIT(_If not installed_)
For Windows:
    
    https://git-scm.com/download/win
    
For MAC OS following the guide under _Installing for MAC_:
    
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    

## Clone API Test GIT Repository:    
    git clone https://github.com/jacqueswest/api_tests.git
    
## Install Required Python Packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
## Executing Tests:
From the root of the repository, run:

**_Ignore the importing ABC from collections DeprecationWarning_**

    pytest

## Output Example:
    tests/test_get_dog_breeds.py::test_get_all_breeds PASSED                                                             [ 25%]
    tests/test_get_dog_breeds.py::test_verify_retriever_breed PASSED                                                     [ 50%]
    tests/test_get_dog_breeds.py::test_get_retriever_sub_breeds PASSED                                                   [ 75%]
    tests/test_get_dog_breeds.py::test_get_random_image_golden_retriever PASSED                                          [100%]

## Viewing Test Report:            
  A report called **_api_report.html_** will be created in the root of the repository after test execution.
  
  Copy the full path of the report and open it in a browser or in a HTML viewer to view the report.
  
  **NB:** Click on _show details_ to see the API response
  
  Example of API HTML test report:
  
    Passed	tests/test_get_dog_breeds.py::test_get_all_breeds	0.91	
    ----------------------------- Captured stdout call -----------------------------
    {'message': {'affenpinscher': [],
                 'african': [],
                 'airedale': [],
                 'akita': [],
                 'appenzeller': [],
                 'basenji': [],
                 'beagle': [],
                 'bluetick': [],
                 'borzoi': [],
                 'bouvier': [],
                 'boxer': [],
                 'brabancon': [],
                 'briard': [],
                 'bulldog': ['boston', 'french'],
                 'bullterrier': ['staffordshire']......
        
