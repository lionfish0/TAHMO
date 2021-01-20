import requests
import json

class TAHMO:
    def __init__(self,baseurl='https://tahmoapi.mybluemix.net/v1'):
        """
        Minimalist wrapper for accessing the TAHMO API (v1).
        
        arguments:
            baseurl = url of the API, default: https://tahmoapi.mybluemix.net/v1
        """
        self.baseurl = baseurl
    def setCredentials(self,api_id,api_secret):
        """
        Set the id and secret needed for access to the API.
        
        arguments:
            api_id = id string
            api_secret = secret string
        """
        self.api_id = api_id
        self.api_secret = api_secret
    def setCredentialsFromJsonFile(self,api_credentials_file):
        """
        If API id and secret are in a json file, can set them directly from the file, e.g:
        tah = TAHMO()
        tah.setCredentialsFromJsonFile('api.json')
        
        arguments:
            api_credentials_file = filename
        """
        api_creds=json.load(open(api_credentials_file,'r'))
        self.setCredentials(api_creds['id'], api_creds['secret'])
    def get_stations(self):
        """
        Get the list of stations you have access to, including various metadata.
        """
        return self.__request('stations')['stations']
    def get_measurements(self,station):
        """
        Get the hourly measurements for a particular station, e.g:
        get_measurements('TA00032")
        
        arguments:
            station = station id string to access.        
        """
        return self.__request('timeseries/%s/hourly' % station)
    def __request(self,endpoint):
        """
            Makes a request to the API for the specified endpoint.
        """
        apiRequest = requests.get("%s/%s" % (self.baseurl,endpoint),                                  
            auth=requests.auth.HTTPBasicAuth(self.api_id, self.api_secret))
        return apiRequest.json()
