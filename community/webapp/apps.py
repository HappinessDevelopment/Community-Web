from django.apps import AppConfig
from os.path import expanduser, join

from stormpath.client import Client as StormpathClient

STORMPATH_API_KEY = join('.stormpath', 'apiKey.properties')
stormpathClient = StormpathClient(api_key_file=STORMPATH_API_KEY)

stormpathClient.application.search({'name': 'webapp'})[0]

class WebappConfig(AppConfig):
    name = 'webapp'
