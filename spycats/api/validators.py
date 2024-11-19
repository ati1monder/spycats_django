import requests

from django.core.exceptions import ValidationError

def breed_validation(breed):
    url = 'https://api.thecatapi.com/v1/breeds'

    try:
        response = requests.get(url)
        response.raise_for_status()
        breeds = [x['name'] for x in response.json()]
    except requests.RequestException as error:
        raise ValidationError(f'Could not validate breed. Error message:\n{error}')
    
    if breed not in breeds:
        raise ValidationError(f'"{breed}" is not recognized.')