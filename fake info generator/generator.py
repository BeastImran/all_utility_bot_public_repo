import json
import requests


"""
The data will be obtained from an api
https://random-data-api.com/api/
Several fake info can be obtained from this api but since
we are generating fake information about a person.
The endpoint will be /users/random_user

"""


def get_fake_info():
    """Get fake information from api"""

    url = 'https://random-data-api.com/api/users/random_user' 
    
    try:
        response = requests.get(url).json()
    except Exception as e:
        return e
    formated_json = json.dumps(response, indent=2)
    return formated_json

