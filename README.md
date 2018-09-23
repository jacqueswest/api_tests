#Setup Guide

##Install Python 3:
Select the latest version from:
    
    
    https://www.python.org/downloads/
    
    
**NB:** For Windows ensure you tick set python path during installation.

##Clone API test GIT repository:
    git clone https://github.com/jacqueswest/api_tests.git
    
##Install required python packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
##Executing tests:
From the root of the repository, run:

    pytest

##Output Example:
    tests/test_get_dog_breeds.py::test_get_all_breeds PASSED                                                             [ 25%]
    tests/test_get_dog_breeds.py::test_verify_retriever_breed PASSED                                                     [ 50%]
    tests/test_get_dog_breeds.py::test_get_retriever_sub_breeds PASSED                                                   [ 75%]
    tests/test_get_dog_breeds.py::test_get_random_image_golden_retriever PASSED                                          [100%]

##Viewing test report:            
  After the test is run, copy the full path of api_report.html and view it in the browser.
  
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
        