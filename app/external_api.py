from functools import lru_cache
from dadata import Dadata

from config import settings


@lru_cache()
def get_country_code_from_dadata(country: str):
    dadata = Dadata(settings.DADATA_TOKEN)
    result = dadata.suggest("country", country)
    try:
        country_code = result[0]['data']['code']
    except Exception as e:
        country_code = None
        print(e)

    return country_code

