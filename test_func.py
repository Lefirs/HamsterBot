from imports import *
from settings import headers

isd = requests.post(url='https://api.hamsterkombat.io/clicker/referral-stat', headers=headers, json={'offset': 0})

print(isd)

print(isd.content)