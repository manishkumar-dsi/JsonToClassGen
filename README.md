# JsonToClassGen
JSON to class generator python library. 

# Description
This is JINJA based command line library. Aim of this library to generate bouler plate code based on a JSON file.
JSON file can be placed on app.py level

# Diractory structure 

## templates
This file contains the JINJA file which is the structure of bouler plate code. As a user you do not need to change it. If you want to add support for new code then create a JINJA file to support this
## types
It contains the mapping between python and language data type. 
## app.py
Main logic
JSON file (ex: data.json)

# What should I do as a user
You only need a data model in JSON format. Keep it on app.py level.
Run the following command line:

- python app.py --lan dart --out out

Here --lan & --out parameters are optional. Class will be generated in out folder. You can change the output directory name by changing the --out parameter value 

## Note
At present this library only support dart classes.