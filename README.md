# TAHMO
Minimalist module for accessing the TAHMO (v1) API. Using the details in https://tahmo.org/docs/TAHMO_API_documentation_latest.pdf
Uses some of the ideas from https://github.com/TAHMO/API-V1-Python-examples and https://github.com/TAHMO/API-V2-Python-examples/blob/master/TAHMO/__init__.py

# Installation
pip install git+https://github.com/lionfish0/TAHMO.git

# Usage
Example:

        from TAHMO import TAHMO
        tah = TAHMO()
        tah.setCredentialsFromJsonFile('apikey.json')
        stations = tah.get_stations()
        
        data = {}
        for s in stations:
            data[s['id']] = tah.get_measurements(s['id'])
