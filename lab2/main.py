import redis
from src import View
from src import Controller


def main():

    r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
    view = View.View()
    c = Controller.Controller(view, r)
    c.parse_user_input()

    # print(f'Hi, Redis')
    # p = r.pipeline()
    # users = "users"
    # login = "maxonn"
    # role = "user"
    # p.hset('%s:%s' % (users, login), mapping={'login': login})
    # p.execute()


if __name__ == '__main__':
    main()

