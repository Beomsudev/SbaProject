# url, parser, path, api, apikey ==> 전부 str type


from dataclasses import dataclass


class Entity:
    url: str = ''
    parser: str = ''
    path: str = ''
    api:str = ''
    apikey:str = ''
