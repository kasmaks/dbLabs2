from datetime import datetime
from . import client
from . import staticData

r = client.r


def create_message(login_from, login_to, body):
    p = r.pipeline()
    login_of_messages = "_from_" + login_from+"_to_" + login_to + "_" + str(datetime.today())
    p.hset(login_of_messages, '_from', login_from)
    p.hset(login_of_messages, '_to', login_to)
    p.hset(login_of_messages, 'date_of_creating', str(datetime.today()))
    p.hset(login_of_messages, 'body', body)
    p.zincrby(staticData.list_of_active_users, 1, login_from)
    p.lpush(staticData.list_of_created_messages, login_of_messages)
    p.rpush(staticData.queue, login_of_messages)

    p.publish(staticData.list_of_created_messages, login_of_messages)

    p.execute()
