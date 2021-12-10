# Github Mock Api
This sample project would allow you to understand basic pytest run along with Allure reporting

Please make sure you have Python, Java installed on your machine beforehand

# How to install pytest
1. pip install pytest

# How to install allure
1. Download allure commandline from: https://mvnrepository.com/artifact/io.qameta.allure/allure-commandline/2.8.1
2. Unzip the directory and put the path of bin to PATH in environment variables
3. pip install allure-pytest


# How to run the code via cmd
pytest -v -s --alluredir=reports

# How to view reports
1. allure serve reports