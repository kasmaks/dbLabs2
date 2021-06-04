from . import client
from . import staticData

r = client.r


def log_events():
    end = r.llen(staticData.log_events)
    list_of_spammers = r.lrange(staticData.log_events, 0, end)
    for el in list_of_spammers:
        print(el)
    input()


def list_of_online_users():
    print("list_of_online_users")
    input()


def rating_of_active_users():
    print("rating_of_active_users")
    amount = r.zcard(staticData.list_of_active_users)
    list_of_active_users = r.zrange(staticData.list_of_active_users, 0, amount, True, True)
    for el in list_of_active_users:
        print(el)
    input()

    input()


def rating_of_active_spammers():
    print("rating_of_active_spammers")
    amount = r.zcard(staticData.list_of_spammers)
    list_of_spammers = r.zrange(staticData.list_of_spammers, 0, r.zcard(staticData.list_of_spammers), True, True)
    for el in list_of_spammers:
        print(el)
    input()
