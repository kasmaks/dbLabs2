from datetime import datetime
from . import client
from . import staticData

r = client.r


def create_user(login, is_admin, password="-1",):
    p = r.pipeline()
    p.hset(login, 'online', "True")
    p.hset(login, 'date_of_registration', str(datetime.now()))
    p.hset(login, 'is_admin', str(is_admin))
    p.sadd(staticData.list_of_users, login)
    if is_admin:
        p.hset(login, 'password', password)
    p.execute()


def get_user(login):
    return r.hgetall(login)
