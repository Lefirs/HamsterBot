from imports import *
from settings import headers


def auto_sync():
    requests.post(url="https://api.hamsterkombat.io/auth/me-telegram", headers=headers)
    requests.post(url="https://api.hamsterkombat.io/clicker/config", headers=headers)
    requests.post(url="https://api.hamsterkombat.io/clicker/sync", headers=headers)
    requests.post(url="https://api.hamsterkombat.io/clicker/upgrades-for-buy", headers=headers)
    requests.post(url="https://api.hamsterkombat.io/clicker/list-tasks", headers=headers)
    requests.post(url="https://api.hamsterkombat.io/clicker/list-airdrop-tasks", headers=headers)