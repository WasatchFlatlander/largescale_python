# -*- coding: utf-8 -*-

# setting up a virtual enviroment
#python -m venv my_virt_env_name
#creates a folder with all the tools needed to import new packages and run a 
#sandboxed python version.

#WINDOWS ACTIVATION
source my_virt_env_name\Scripts\activate.bat
#LINUX
source my_virt_env_name/bin/activate

#get python version
python -V
which python #location of python
which pip #location of pip

#DEACTIVATE environment
deactivate

pip freeze > requirements.txt # puts current virtual environment packages installed. 
# put this file into virtual environment


(my_virtual_env_name) pip install -r requirements.txt #Installs necessary packages


######PIPFILE#############
pipenv install pandas
- create a virtual environment if not already there
- records the high level requirement of pandas into Pipfile
- generate a Pipfile.lock with exact version control and its dependencies
- Any future uninstall will remove unneeded dependencies


