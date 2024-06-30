import requests

from imports import *
from settings import headers

def code_write(code):
    requests.post(url='https://api.hamsterkombat.io/clicker/claim-daily-cipher', headers=headers, json={'cipher': code})