'''
Created on Aug 31, 2017

@author: joseph_sicree
'''
import simpleapi
import requests
from requests.auth import HTTPBasicAuth

def main():
#     print("Compute = ", compute(1,2))
#     
#     getAllCountries()
    getState('MA')
    
    
def compute(val1, val2):
    return(val1 + val2)

def getAllCountries():
    
    url = 'http://localhost:8080/springweb/api/reference/v1/getAllCountries'
    response = requests.post(url,auth=HTTPBasicAuth('user', 'password'))
    print(response.json())

        
def getState(code):    

    url = 'http://localhost:8080/springweb/api/reference/v1/getStateByCode'
    headers = {'Accept': 'application/json'}
    response = requests.post(url,auth=HTTPBasicAuth('user', 'password'), data={'stateCode':'MA'}, headers=headers)
    print(response)
    
#     stateDto = simpleapi.StateDto()
#     stateDto.id = 1
#     stateDto.code = code
#     stateDto.name = "Mass"     
#     return stateDto
    
    
main()

    